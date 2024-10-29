import os
from dotenv import load_dotenv

load_dotenv()

BEDROCK_REGION = os.getenv('BEDROCK_REGION', 'us-west-2')
MODEL_ID = os.getenv('MODEL_ID', 'anthropic.claude-3-5-sonnet-20241022-v2:0')
SYSTEM_PROMPT_PATH = os.path.join(os.path.dirname(__file__), '..', 'agent', 'system_prompt.txt')
