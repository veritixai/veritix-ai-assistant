from pypdf import PdfReader


def read_pdf(file):

    file.seek(0)

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def get_pdf_statistics(file, text):

    file.seek(0)

    reader = PdfReader(file)

    pages = len(reader.pages)

    words = len(text.split())

    characters = len(text)

    reading_time = max(1, round(words / 250))

    return {
        "pages": pages,
        "words": words,
        "characters": characters,
        "reading_time": reading_time,
    }