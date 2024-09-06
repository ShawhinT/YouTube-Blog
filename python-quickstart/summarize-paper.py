# code that extracts text from a pdf file and sends generates a summary and keywords

import fitz  # PyMuPDF
import openai
import sys
from sk import my_sk

# Set up your OpenAI API key
openai.api_key = my_sk

# Function to read the first page of a PDF and extract the abstract
def extract_abstract(pdf_path):
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        first_page = pdf[0]
        text = first_page.get_text("text")
    
    # Extract the abstract (assuming the abstract starts with 'Abstract')
    # You can adjust this based on the PDF structure
    start_idx = text.lower().find('abstract')
    end_idx = text.lower().find('introduction') if 'introduction' in text.lower() else None

    if start_idx != -1:
        abstract = text[start_idx:end_idx].strip()
        return abstract
    else:
        return None

# Function to summarize the abstract and generate keywords using OpenAI API
def summarize_and_generate_keywords(abstract):
    if not abstract:
        return None, None
    
    # Use OpenAI Chat Completions API to summarize and generate keywords
    prompt = f"Summarize the following paper abstract and generate (no more than 5) keywords:\n\n{abstract}"
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ], 
        temperature = 0.25
    )
    
    summary = response.choices[0].message.content
    return summary


# Get the PDF path from the command-line arguments
pdf_path = sys.argv[1]

# Extract abstract from the PDF
abstract = extract_abstract(pdf_path)

if abstract:
    # Summarize and generate keywords
    summary = summarize_and_generate_keywords(abstract)
    
    print(summary)
else:
    print("Abstract not found on the first page.")
