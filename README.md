# Text Summarizer

A simple AI-powered text summarizer built with Python and Streamlit.  
This project allows users to input text or upload PDFs and get concise summaries using Hugging Face models.

---

## Features
- Summarize text from input box
- Summarize text from PDF files
- Clean and minimal Streamlit interface
- Easy to run locally or deploy later

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aryankhatri02/text_summarizer.git
cd text_summarizer


python -m venv venv

2. Create a virtual environment:
python -m venv venv


3. Activate the virtual environment:
windows(powershell)
.\venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt


Usage

1. Run the Streamlit app:

streamlit run app.py


2. Open the provided local URL in your browser (usually http://localhost:8501).

3. Enter text or upload a PDF and get a summarized version instantly.


Project Structure
text_summarizer/
│
├── app.py           # Streamlit interface
├── summarizer.py    # Summarization logic
├── pdf_utils.py     # PDF handling (optional)
├── requirements.txt # Python dependencies
├── .gitignore       # Git ignore rules
└── README.md        # Project documentation


