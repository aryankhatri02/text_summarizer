import streamlit as st
from summarizer import summarize_text
from pdf_utils import extract_text_from_pdf

st.set_page_config(page_title="AI Text Summarizer", layout="wide")

st.title("📄 AI Text Summarizer")

option = st.radio("Choose input type:", ["Text", "PDF"])

summary = None  # placeholder

if option == "Text":
    input_text = st.text_area("Paste your text here:", height=200)
    if st.button("Summarize"):
        if input_text.strip():
            summary = summarize_text(input_text)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

elif option == "PDF":
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None and st.button("Summarize PDF"):
        text = extract_text_from_pdf(uploaded_file)
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)

# ✅ Add download button if summary exists
if summary:
    st.download_button(
        label="📥 Download Summary",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )
