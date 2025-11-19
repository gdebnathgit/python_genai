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


def classify_patient(patient_info):
    """
    patient_info is a dict. Example:
    {
        "age": 65,
        "condition": "Severe chest pain, irregular heartbeat",
        "vitals": {"bp": "80/60", "pulse": 140},
        "notes": "Patient brought from ER"
    }
    """

    prompt = f"""
You are a medical triage support assistant.
Classify the patient into one of these categories:

1. CRITICAL: Immediate attention (ICU, emergency)
2. MODERATE: Needs observation (post-op, surgical)
3. STABLE: Minimal intervention (routine check-up)

Return ONLY this JSON format:
{{
  "category": "<Critical | Moderate | Stable>",
  "reason": "<short explanation>"
}}

Patient Data:
{patient_info}
"""

    response = llm.invoke(prompt)

    return response.text


if __name__ == "__main__":
    patient = {
        "age": 65,
        "condition": "Severe chest pain, irregular heartbeat",
        "vitals": {"bp": "80/60", "pulse": 140},
        "notes": "Arrived at ER"
    }

    result = classify_patient(patient)
    print("Classification Result:")
    print(result)
