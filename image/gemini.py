from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")


def default_display(output):
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

    # if fields:
    #     extracted_data = {}
    #     for field_name, example in fields.items():
    #         field_text = None
    #         if example in extracted_text:
    #             field_start = extracted_text.find(example)
    #             if field_start != -1:
    #                 field_end = extracted_text.find("\n", field_start)
    #                 if field_end != -1:
    #                     field_text = extracted_text[field_start:field_end].strip()
    #         extracted_data[field_name] = field_text
    #     return extracted_data
    # else:
        # return default_display(extracted_text)
    return default_display(extracted_text)


st.set_page_config(page_title="Gemini pro vision")

st.header("TEXT FROM IMAGE CROELHO PLAYGROUND")
uploaded_file = st.file_uploader("Insert an image...", type=["jpg", "jpeg", "png", "pdf"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

fields_input = st.text_area("Enter fields and examples (in JSON format):")

fields = None
if fields_input:
    try:
        fields = json.loads(fields_input)
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please enter fields and examples in valid JSON format.")

if fields is not None:
    for field_name, example in fields.items():
        field_input = st.text_input(f"Enter example for {field_name}:", value=example)

if uploaded_file is not None and fields is not None:
    response = gemini_response(image, fields)
    st.subheader("TEXT FROM INPUT:")
    st.write(response)
