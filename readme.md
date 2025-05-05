# The application
Basic idea: simulated chat between the customer service ``Employee`` of a travel agency (named Tom), a Customer and Assistant Bob, the LLM who assists Tom.
Sequence diagram: [here](https://www.mermaidchart.com/app/projects/c4efd5c1-213b-487e-ab6b-f5a2c2c60c03/diagrams/537b8f77-d121-4d31-ae29-a0ee7df9c6db/version/v0.1/edit)


# How to start the API and front-end
* Create a .env from .env.dist file, and add your OpenAI api key
* Create / activate your virtual env and set it up : ``$pip install -r requirements.txt``
* To start the API: ``$python main.py`` (go to http://127.0.0.1:8000/docs to access it Swagger UI)
* To start the front-end: ``$python -m http.server 5500`` (at the root of `/front-end-app` !)


# The LLM used, and why
* I used OpenAI `gpt-4.1-nano` because:
  * OpenAI models are known to be efficient, and there are a lot a ressources about how to use them
  * no need for a reasoning model here
  * `gpt-4.1-nano` just came out, and it's presented as their fastest (and cheapest) model, that delivers good performance at generating answers following various instructions, and has a large context window (1 million tokens), which seems particularly suited for this chat app.
  * also... "OpenAI’s API conveniently lets us provide the name of the participant for each message in the conversation" according to this [post](https://towardsdatascience.com/ai-for-groups-build-a-multi-user-chat-assistant-using-7b-class-models-7071ca8b4aa0/), though I ended up using OpenAI tools that do not implement this feature ^^ 
* I used their [Responses](https://platform.openai.com/docs/api-reference/responses) API to query the LLM (see this [comparison](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses) with Chat Completions API)


# Key prompt design strategy for the multi-user context
* Structure -> follows OpenAI [prompting guidelines](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)
* It includes :
  * A system prompt, with few-shots examples
  * A reminder prompt for key instructions passed as context under the "role" of ``developer``
* Key instructions include:
  * Not to answer at all rounds, but only if it, as Assistant Bob, has something relevant to say
  * To name the user it's responding to
  * To provide its full answer at once instead of saying e.g. "let me check if..." or "give me a moment for ..."

# Management of conversation history
Chat session history is managed and provided to the LLM :
* stored in a "database", using a chat session_id -> each new message sent is stored in a (for now) dict object -> constitutes chat history (improvement: use a 'real' DB instead, e.g. Cassandra, often mentioned for storing chat history)
* not all chat history is sent as context to the LLM, instead it is limited to a given number tokens or messages, or a given conversation duration (improvement: RAG, to add older messages that are relevant regarding the topic of the last message)
* It is provided to the LLM as a dialog-like text, in the context ("input"), under the "role" `user` (as [this OpenAI feature](https://platform.openai.com/docs/guides/conversation-state#manually-manage-conversation-state) is not fitted for multi-user conversation)


# Challenges faced
* Windows 🙄
* LLM:
  * LLM not adressing the right user -> instructions in system prompt (maybe a bit drastic)
  * LLM's natural tone in general (would still need improvement), and specifically
    * adressing users by their name -> instructions in system prompt, result not ideal but better
    * saying hello -> reminder prompt + postprocessing
    * not always answering -> reminder prompt
    * saying "give me a moment for ..." -> instructions in system prompt
  * left unsolved:
    * do not always answer when directly asked despite instruction in system prompt
    * do not always answer when it could -- to explore for potential improvement:
      * ask LLM for message + probability of relevance -> control on the threshold to send (or not) the message
      * regex on input message to detect e.g. "Bob" or "assistant", and when regex detected, retry the LLM query until we get a message
* front-end:
  * everything ^^ --> architecture/flow that gathers a max of complexity in the back end
  * For the first time, I could say "I have a CORS problem" -- for the first time too, I had a rough idea of what it meant -> CORS activated on back-end side


# Not done yet / to be improved:
* Errors handling
* Real DB for chat history and users (e.g. Cassandra or relational)
* Adaptive personality -> possible ways:
  * pipeline with
    * sentiment analysis of the user message by an LLM (among given list of sentiment)
    * mapping between sentiment detected <> assistant tone
    * assistant tone passed in a new instruction in prompt
  * Chain of Thought: same steps, but done by the same LLM in a single request
* front-end -> unfinished, and more than very simple for now as it is my first front-end development :) 

# Experience learning JavaScript
I can't say I've learned it yet, though what I did is:
* do 2 less than 1 hour tutorial on JS basics
* [ask ChatGPT](https://chatgpt.com/c/6817bdc7-43fc-8005-963d-398b7a70e730) to provide me with a project basis and to explain me what each line does
* adapt this basis to the flow I had in mind (cf [sequence diagram](https://www.mermaidchart.com/app/projects/c4efd5c1-213b-487e-ab6b-f5a2c2c60c03/diagrams/537b8f77-d121-4d31-ae29-a0ee7df9c6db/version/v0.1/edit)), first by "trying things", and asking ChatGPT again when I got stuck