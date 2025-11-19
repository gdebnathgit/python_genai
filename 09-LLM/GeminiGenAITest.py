import google.generativeai as genai
import logging as log

log.getLogger("google.auth").setLevel(log.ERROR)

genai.configure(api_key="AIzaSyAR9ggkWZyMaWUIUYJIgvBz4XJMpPuhb-4")

"""
# List all available models
models = genai.list_models()

# Print model names and supported methods
for model in models:
    print(f"Model Name: {model.name}")
    print(f"Supported Methods: {model.supported_generation_methods}")
    print("-" * 40)

"""

# Choose the Gemini model (e.g., gemini-1.5-pro or gemini-1.5-flash)
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash-preview-05-20")

# Send a prompt to the model
response = model.generate_content(
    "Mention the state name from India where kolkata.")

# Print the response
print(response.text)
