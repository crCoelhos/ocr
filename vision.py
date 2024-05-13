from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image


load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model=genai.GenerativeModel("gemini-pro-vision")


def gemini_response(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
        response = model.generate_content([image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini pro vision")

st.header("TEXT FROM IMAGE CROELHO PLAYGROUND")
uploaded_file = st.file_uploader("Insert an image...", type=["jpg", "jpeg", "png", "pdf"])
image=""   

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


# submit=st.button("EXTRACT TEXT")


if uploaded_file is not None:
    response=gemini_response(image)
    st.subheader("TEXT FROM INPUT:")
    st.write(response)