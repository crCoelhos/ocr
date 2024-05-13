from PIL import Image
import pytesseract
import streamlit as st


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Configurações do Streamlit
st.set_page_config(page_title="OCR Playground")

# Função para extrair texto da imagem usando OCR
def extract_text(image):
    # Usa o pytesseract para extrair texto da imagem
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

# Interface do Streamlit
st.title("OCR Playground")
uploaded_file = st.file_uploader("Carregar imagem", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Abre a imagem carregada
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem carregada", use_column_width=True)

    # Extrai texto da imagem
    text = extract_text(image)

    # Exibe o texto extraído
    st.header("Texto extraído da imagem:")
    st.write(text)
