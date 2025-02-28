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


# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load OpenAI model and get respones
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response =chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini Application")

# input=st.text_input("Input: ",key="input")


# submit=st.button("Ask the question")

# ## If ask button is clicked

# if submit:
    
#     response=get_gemini_response(input)
#     st.subheader("The Response is")
#     for chunk in response:
#         print(st.write(chunk.text))
#         print("_"*80)
    
#     st.write(chat.history)


import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit UI
st.set_page_config(page_title="Q&A Chat")
st.header("Chat with Gemini")

# User Input
user_input = st.text_input("Your Message:")
if st.button("Send") and user_input.strip():
    response = get_gemini_response(user_input)

    st.subheader("Bot Response:")
    response_text = ""
    for chunk in response:
        response_text += chunk.text
        st.write(chunk.text)

    # Save to session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response_text))

# Display History
st.subheader("Chat History")
for role, text in st.session_state.get("chat_history", []):
    st.write(f"**{role}:** {text}")
