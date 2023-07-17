from dotenv import load_dotenv
import os
from langchain.llms import AzureOpenAI

# Load the environment variables from the .env file
load_dotenv()

# Get the environment variables
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # make sure this is in your .env file
BASE_URL = os.getenv("BASE_URL")  # make sure this is in your .env file

llm = AzureOpenAI(
    deployment_name="td2",
    model_name="text-davinci-002",
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=OPENAI_API_KEY,  # use the API key here
    base_url=BASE_URL,  # use the base URL here
)

response = llm("Tell me a joke")
print(response)
