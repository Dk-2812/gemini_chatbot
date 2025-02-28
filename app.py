# # Q&A Chatbot
# #from langchain.llms import OpenAI

# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

# import streamlit as st
# import os
# import pathlib
# import textwrap

# import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load OpenAI model and get respones

# def get_gemini_response(question):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(question)
#     return response.text

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini Application")

# input=st.text_input("Input: ",key="input")


# submit=st.button("Ask the question")

# ## If ask button is clicked

# if submit:
    
#     response=get_gemini_response(input)
#     st.subheader("The Response is")
#     st.write(response)

##########


# import os
# import textwrap
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load API Key from .env
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to sanitize input
# def sanitize_input(text):
#     return text.replace("\n", " ").strip()

# # Function to get response
# def get_gemini_response(question):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(sanitize_input(question))
#     return response.text

# # Streamlit UI
# st.set_page_config(page_title="Q&A Demo")
# st.header("Gemini Application")

# # Chat Input
# user_input = st.text_input("Ask your question:", key="input")
# if st.button("Ask"):
#     if user_input.strip():
#         response = get_gemini_response(user_input)
#         st.subheader("Response:")
#         st.write(response)

#############

import os
import textwrap
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Q&A Demo")
st.header("🔐 Secure Gemini Chatbot")

# 🔹 Show API Key Status
if not api_key:
    st.warning("⚠️ API Key is missing! Please check your environment settings.", icon="⚠️")
else:
    st.success("✅ API Key Loaded Successfully", icon="🔑")

# Configure Gemini API
genai.configure(api_key=api_key)

# Function to sanitize input
def sanitize_input(text):
    restricted_words = ["DROP TABLE", "DELETE FROM", "INSERT INTO", "--"]
    for word in restricted_words:
        if word.lower() in text.lower():
            return None  # Block potentially harmful input
    return text.replace("\n", " ").strip()

# Function to get response
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# 🔹 Safe Mode Toggle
safe_mode = st.checkbox("🛡️ Enable Safe Mode (Stricter Security)")

# User Input
user_input = st.text_input("Ask your question:", key="input")
if st.button("Ask"):
    if not user_input.strip():
        st.warning("⚠️ Input cannot be empty!")
    else:
        sanitized_input = sanitize_input(user_input)
        if sanitized_input is None:
            st.error("🚫 Input blocked: Suspicious content detected!")
        else:
            # Rate Limiting: Prevent too many requests
            if "request_count" not in st.session_state:
                st.session_state.request_count = 0
            if st.session_state.request_count >= 5 and safe_mode:
                st.error("🚨 Too many requests! Please wait before asking again.")
            else:
                response = get_gemini_response(sanitized_input)
                st.subheader("🤖 Response:")
                st.write(response)
                st.session_state.request_count += 1

