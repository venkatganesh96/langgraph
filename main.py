import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "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"

llm_azure = ChatOpenAI()
printf("hello world")
