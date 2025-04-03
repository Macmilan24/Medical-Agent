import os
import pdfplumber
import re
from pathlib import Path
from typing import List, Dict


def read_pdf(file_path: str, max_pages: int) -> str:
    """Extract the Text from the PDF file"""

    text = ""
    with pdfplumber.open(file_path) as pdf:
        pages = pdf.pages[:max_pages]
        text = " ".join(page.extract_text() for page in pages if page.extract_text())

    return text


def clean_text(text: str) -> str:
    """Remove unwanted charaters headers, and extra spaces"""

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\d+ of \d+", "", text)

    return text.strip()


def chunk_text(text: str, chuck_size: int = 500) -> List[str]:
    """Split text into smaller chunks for embedding or processing.

    Args:
        text (str): The input text to be split into chunks.
        chunk_size (int, optional): The maximum size of each chunk. Defaults to 500.

    Returns:
        List[str]: A list of text chunks, each with a length up to the specified chunk size.
    """

    chunks = []
    words = text.split()
    for i in range(0, len(words), chuck_size):
        chunk = " ".join(words[i : i + chuck_size])
        chunks.append(chunk)

    return chunks


def process_documents(data_folder: str, max_pages: int) -> List[Dict[str, str]]:
    """Read And process all PDFs in the folder"""
    proccessed_data = []
    for file in Path(data_folder).rglob("*.pdf"):
        text = read_pdf(file, max_pages=max_pages)
        text = clean_text(text)
        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):
            proccessed_data.append(
                {
                    "source": file.name,
                    "chunk_id": f"{file.stem}_chunk{idx}",
                    "text": chunk,
                }
            )
    return proccessed_data
