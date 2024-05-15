from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
import re
import json

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")


def gemini_response(image):
    if image != "":
        response = model.generate_content([image])
    else:
        response = model.generate_content(image)
    return response.text


def extract_name_and_age(text, ocr_text):
    name_pattern = r'O nome dela é ([A-Za-z]+(?:\s+[A-Za-z]+)*)'
    age_pattern = r'(\d+)'

    name_match = re.search(name_pattern, ocr_text)
    age_match = re.search(age_pattern, text)

    if name_match:
        name = name_match.group(1)
    else:
        name = "Nome não encontrado"

    if age_match:
        age = age_match.group(1)
    else:
        age = "Idade não encontrada"

    # return {"name": name, "age": age, "raw_ocr_text": ocr_text}
    return {"raw_ocr_text": ocr_text}


st.set_page_config(page_title="Gemini pro vision")

st.header("CROELHO PLAYGROUND")
uploaded_file = st.file_uploader("Insert an image...", type=["jpg", "jpeg", "png", "pdf"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

if uploaded_file is not None:
    response = gemini_response(image)
    extracted_info = extract_name_and_age(response, response)
    extracted_info_json = json.dumps(extracted_info)
    st.subheader("Respnse:")
    st.write(extracted_info_json)
