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
    deployment_name="gpt35",
    model_name="gpt-35-turbo",
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=OPENAI_API_KEY,  # use the API key here
    model_kwargs={"base_url": BASE_URL},  # pass base_url as part of model_kwargs
)

response = llm("Tell me a joke")
print(response)
