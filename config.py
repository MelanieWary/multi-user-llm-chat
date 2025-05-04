import os

from dotenv import load_dotenv

load_dotenv()


MODEL = os.environ["MODEL"]
DURATION_MAX = int(os.environ["CONTEXT_DURATION_MAX"])
TOKENS_MAX = int(os.environ["CONTEXT_TOKENS_MAX"])
MESSAGES_MAX = int(os.environ["CONTEXT_MESSAGES_MAX"])
