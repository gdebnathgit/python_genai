# Create virtual environment for the python project
python -m venv .venv 

# Set execution policy for the current user
python -m venv .venv 

# Update pip module
python.exe -m pip install --upgrade pip

# Package install
pip install streamlit 
pip install langchain
pip install langchain-google-genai google-generativeai python-dotenv

pip list

pip uninstall langchain-core


langchain 1.0.7 requires langchain-core<2.0.0,>=1.0.4, but you have langchain-core 0.3.79 which is incompatible.
langgraph-prebuilt 1.0.4 requires langchain-core>=1.0.0, but you have langchain-core 0.3.79 which is incompatible.

jsonschema                   4.25.1
jsonschema-specifications    2025.9.1
langchain                    1.0.7
langchain-core               0.3.79
langchain-google-genai       2.0.10
langgraph                    1.0.3
langgraph-checkpoint         3.0.1
langgraph-prebuilt           1.0.4
langgraph-sdk                0.2.9