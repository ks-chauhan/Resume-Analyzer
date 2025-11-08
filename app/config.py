import os
from dotenv import load_dotenv

load_dotenv()

# load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# model configurations
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "gpt-5-nano"
