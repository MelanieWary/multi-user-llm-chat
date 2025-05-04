# How to start the API
* create a .env from .env.dist file, and add your OpenAI api key
~~* `$source .env`~~
* `$pip install -r requirements.txt`
* To start the  API:   or `$python main.py`
* Then go to http://127.0.0.1:8000/docs for Swagger UI


# Sequence diagram
XXXXXXXXXXXXXXXXXXXXXXXXX


# LLM used, and why
* OpenAI, gpt-4.1-nano
* 


# Prompt design strategy for the multi-user context
* Structure -> follows OpenAI [prompting guidelines](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)
* Few-shots examples
* Reminder prompt for key instructions passed as context une the role of ``developer``

# Management of conversation history
how I managed and provided conv history to the LLM
* chat session_id -> each new message sent is stored in a (for now) dict object -> constitutes chat history (improvement: use a 'real' DB instead, e.g. Cassandra, often mentioned for storing chat history)
* limit to nb tokens, nb messages, conv duration (improvement: RAG, to add older messages that are relevant regarding the topic of the last message)
* passed in context, as dialog-like, under the role `user` -> there is [this](https://platform.openai.com/docs/guides/conversation-state#manually-manage-conversation-state) but not fitted for multi-user


# Challenges faced
* Windows 🙄
* LLM not adressing the right user -> instructions in system prompt (maybe a bit drastic)
* natural tone in general (would still need improvement), and specifically
  * adressing users by their name -> instructions in system prompt, result not ideal but better
  * say hello -> reminder prompt + PP
  * not always answering -> reminder prompt
  * saying "give me a moment for ...." -> instructions in system prompt
* left unsolved:
  * do not always answer when directly asked despite instruction in system prompt
  * do not always answer when it could -- potential improvment through:
    * ask LLM for message + proba of relevance -> control on the threshold to send (or not) the message


# Not done yet / to be improved:
* Errors handling
* Real DB for chat history and users (e.g. Cassandra or relational)
* Adaptive personality -> possible ways:
  * pipeline with
    * sentiment analysis of the user message by an LLM (among given list of sentiment)
    * mapping between sentiment detected <> assistant tone
    * assistant tone passed in a new instruction in prompt
  * Chain of Thought: same steps, but done by the same LLM in a single request


# Experience learning TypeScript/JavaScript