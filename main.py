
import pdf_to_text as pdf

def get_started(FILE_PATH):
    response=pdf.covert_to_text(FILE_PATH)
    return response