from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model=genai.GenerativeModel("gemini-pro")

def gemini_responsr(input):
    response = model.generate_content(input)
    return response.text

st.set_page_config(page_title="TESTE")

st.header("TESTE COM LLM DO GEMINI")

input=st.text_input("insert a input: ", key="input")
submit=st.button("Submit")

if submit:
    response=gemini_responsr(input)
    st.write(response)