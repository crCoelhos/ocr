instalar python3
instalar o tesseract (se for usara o tesseract), através do: https://github.com/UB-Mannheim/tesseract/wiki
fazer copia da .env.example se for usar gemini OCR, via:

    cp .env.example .env

depois checar a env para preenchimento;

criar venv:

    python3 -m venv venv

ativar venv:

    venv\Scripts\activate

instalar os requisitos:

    pip install -r requirements.txt

executar via:

    streamlit run path/file.py
