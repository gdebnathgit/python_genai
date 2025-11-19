import os
from dotenv import load_dotenv
from langchain_core.globals import set_debug
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import Chroma
from langchain_chroma import Chroma
# from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatGoogleGenerativeAI


"""
# Install module name
# pip install langchain langchain-community google-generativeai chromadb

"""

# Load environment variables from .env file
load_dotenv()
set_debug(False)

# Access the API key
google_api_key = os.getenv("GOOGLE_API_KEY")


# Load and split documents
loader = TextLoader("data/your_docs.txt")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Embed and store in Chroma
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(chunks, embedding)
