import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.globals import set_debug
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()
set_debug(False)

# Access the API key
google_api_key = os.getenv("GOOGLE_API_KEY")
# print(google_api_key)

# Initialize the ChatGoogleGenerativeAI model
# You can specify the model (e.g., 'gemini-pro', 'gemini-pro-vision')
# and other parameters like temperature.
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", google_api_key=google_api_key, temperature=0.7, verbose=False)


# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful AI assistant that answers questions accurately."),
#     ("user", "{user_input}")
# ])
# chain = prompt | llm
# user_question = "What is the capital of France?"
# response = chain.invoke({"user_input": user_question})
# print(response.content)

# First chain: Get a city based on a person
city_prompt = ChatPromptTemplate.from_messages([
    ("human", "Where is {person} from? Respond with just the city name.")
])

city_chain = city_prompt | llm | StrOutputParser()

# Second chain: Get the country of that city
country_prompt = ChatPromptTemplate.from_messages([
    ("human", "What country is {city} in? Respond in {language}.")
])

country_chain = country_prompt | llm | StrOutputParser()

# Combine the chains
full_chain = {"city": city_chain,
              "language": lambda x: x["language"]} | country_chain

# Invoke the full chain
result = full_chain.invoke(
    {"person": "Albert Einstein", "language": "English"})
print(result)
