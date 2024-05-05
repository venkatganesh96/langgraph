import os
from langchain.chat_models import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings

os.environ["AZURE_OPENAI_ENDPOINT"] = "https://openaitrials.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "f7e330db85eb4ca5855620ca2656871e"

embeddings = AzureOpenAIEmbeddings(
    azure_deployment="textembeddingad002dep2",
    openai_api_version="2023-07-01-preview",
)

llm_azure = AzureChatOpenAI(openai_api_version="2023-07-01-preview",
                            azure_deployment='gpt35turbo16kdep2',
                            temperature=0
                            )
printf("hello world")
