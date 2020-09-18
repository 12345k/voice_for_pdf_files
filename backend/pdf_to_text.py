import PyPDF2 
# import text_to_voice

def covert_to_text(FILE_PATH):
    result=""
    with open(FILE_PATH, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        print(f"Number of pages: {reader.getNumPages()}")

        
        for i in range(reader.getNumPages()):
            pageObj = reader.getPage(i-1)
            raw_text = pageObj.extractText() 
            print(raw_text)
            result+=" "+raw_text
            # text_to_voice.read(raw_text)
            
            print("*"*100)
    return result

# covert_to_text("/home/karthickaravindan/pdf_audio_reader/backend/pdf_files/tmps5hcz01j.pdf")