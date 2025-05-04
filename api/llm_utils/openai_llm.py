"""Utils to query OpenAI LLM"""
from loguru import logger
from openai import OpenAI
import tiktoken
from typing import List, Union

from api.common.data_models import ContextUnit
from config import MODEL


llm_client = OpenAI()

def query_llm(system_prompt:str, context: Union[str, List[ContextUnit]]):
    logger.info("Querying LLM")
    try :
        response = llm_client.responses.create(
            model=MODEL,
            instructions=system_prompt,
            input=context,
        )
    except Exception as exc:
        logger.info(f"Could not query the llm -- error: {exc}")
        raise Exception
    return response

# get llm encoding for token estimate
# encoding = tiktoken.encoding_for_model(MODEL)  # model "gpt-4.1-nano"not found yet
ENCODING = tiktoken.get_encoding("cl100k_base")
