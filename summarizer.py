from transformers import pipeline
from pdf_utils import extract_text_from_pdf

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_tokens=800):
    """Split text into smaller chunks so the model can handle them."""
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i + max_tokens])

def summarize_text(text):
    summaries = []
    for chunk in chunk_text(text):
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return " ".join(summaries)

if __name__ == "__main__":
    # Example with plain text
    text = """
    Artificial intelligence is rapidly transforming the world. 
    Large language models are now capable of generating human-like text, 
    assisting with tasks such as summarization, translation, and even software development. 
    Companies are adopting AI to improve productivity and innovation across multiple domains.
    """
    print("Text Summary:", summarize_text(text))

    # Example with PDF
    pdf_text = extract_text_from_pdf("sample.pdf")  # replace with your PDF file
    print("PDF Summary:", summarize_text(pdf_text))
