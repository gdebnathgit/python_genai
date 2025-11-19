from google import genai

"""
Generetive AI call using goole genai

# Install package list
# pip install google-genai

"""

# The client automatically picks up the API key from the GEMINI_API_KEY environment variable.
client = genai.Client(api_key="AIzaSyAR9ggkWZyMaWUIUYJIgvBz4XJMpPuhb-4")

# Specify the model you want to use
model_id = "gemini-2.5-flash"  # Or another available model like 'gemini-1.5-flash'

# Send a prompt to the model
response = client.models.generate_content(
    model=model_id,
    contents="Mention the state name from India where kolkata."
)

# Print the model's response
print(response.text)
