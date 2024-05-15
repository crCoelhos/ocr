from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")


def default_display(output):
    # Aqui você pode definir um modelo de exibição padrão para o output.
    # Neste exemplo, formatamos o texto no formato chave-valor.
    lines = output.split("\n")
    formatted_output = ""
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            formatted_output += f"{key.strip()}: \"{value.strip()}\";\n"
    return formatted_output


def gemini_response(image, fields=None):
    response = model.generate_content([image])
    extracted_text = response.text

    if fields:
        extracted_data = {}
        for field_name, example in fields.items():
            field_text = None
            for line in extracted_text.split('\n'):
                if example in line:
                    field_text = line.replace(example, '').strip()
                    break
            extracted_data[field_name] = field_text
        return extracted_data
    else:
        return default_display(extracted_text)


st.set_page_config(page_title="Gemini pro vision")

st.header("TEXT FROM IMAGE CROELHO PLAYGROUND")
uploaded_file = st.file_uploader("Insert an image...", type=["jpg", "jpeg", "png", "pdf"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Definir inputs para nome da chave e exemplo de valor para cada campo
fields = {}
if uploaded_file is not None:
    st.subheader("Enter fields and examples:")
    while True:
        field_name = st.text_input("Enter field name (leave empty to stop):")
        if not field_name:
            break
        example = st.text_input(f"Enter example for {field_name}:")
        if field_name.strip() != "":
            fields[field_name] = example

if uploaded_file is not None and fields:
    response = gemini_response(image, fields)
    st.subheader("TEXT FROM INPUT:")
    st.write(response)
