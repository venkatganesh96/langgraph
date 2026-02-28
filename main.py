import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk"

llm_azure = ChatOpenAI()
printf("hello world")
