import os
import bs4
from dotenv import load_dotenv
from langchain_core.globals import set_debug
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langchain.agents import create_agent


"""
# https://docs.langchain.com/oss/python/langchain/rag#chroma
# Install module name
# pip install dotenv
# pip install langchain langchain-community langchain-text-splitters 
# pip install bs4
# pip install langchain_core.globals langchain_google_genai 
# pin install langchain_chroma

"""

# Load environment variables from .env file
load_dotenv()
set_debug(False)

# Access the API key
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", google_api_key=google_api_key, temperature=0.7, verbose=False)

# Initialize the GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# Embed and store in Chroma
vector_store = Chroma(
    collection_name="rag_collection",
    embedding_function=embeddings,
    # Where to save data locally, remove if not necessary
    persist_directory="./ChromaDB/chroma_langchain_db",
)

# Only keep post title, headers, and content from the full HTML.
bs4_strainer = bs4.SoupStrainer(
    class_=("post-title", "post-header", "post-content"))
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs={"parse_only": bs4_strainer},
)
docs = loader.load()

# Create splited text for chunk creation
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents(docs)

# Add splited chunk into vector DB
document_ids = vector_store.add_documents(documents=all_splits)

# create a retrived tool to read data from vector db as per query


def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that retrieves context from a blog post. "
    "Use the tool to help answer user queries."
)
agent = create_agent(llm, tools, system_prompt=prompt)

# query = (
#     "What is the standard method for Task Decomposition?\n\n"
#     "Once you get the answer, look up common extensions of that method."
# )

query = "What is task decomposition?"

response = agent.invoke({"messages": [{"role": "user", "content": query}]})
response["messages"][-1].pretty_print()
