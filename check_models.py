# import google.generativeai as genai

# genai.configure(api_key="AIzaSyDNMjMv_wjISl8-9-CQUU-DbtfRXhOpYXk")

# models = genai.list_models()
# for model in models:
#     print(model.name)

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
models = genai.list_models()
for model in models:
    print(model.name)
