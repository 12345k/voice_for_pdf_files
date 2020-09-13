from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import aiofiles
import random
import os
import pdf_to_text

app = FastAPI()

STORAGE_PATH = 'pdf_files'



@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    result=""
    for file in files:
        fpath = os.path.join(
            STORAGE_PATH, f'{file.filename}'
        )
        async with aiofiles.open(fpath, 'wb') as f:
            content = await file.read()
            await f.write(content)

        pages=pdf_to_text.covert_to_text(os.path.join(
            STORAGE_PATH, f'{file.filename}'
        ))
        

    return {"message": pages}

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
