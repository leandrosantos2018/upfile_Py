from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import List
import shutil
import os

app = FastAPI()

# Diretório onde os arquivos serão salvos
UPLOAD_DIRECTORY = "uploaded_files"

# Crie o diretório, se não existir
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    file_names = []
    for file in files:
        # Caminho completo onde o arquivo será salvo
        file_location = f"{UPLOAD_DIRECTORY}/{file.filename}"

        # Salva o arquivo no diretório
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        file_names.append(file.filename)

    return {"message": "Arquivos enviados com sucesso", "files": file_names}

@app.get("/")
async def main():
    content = """
    <html>
        <body>
            <h2>Upload de múltiplos arquivos</h2>
            <form action="/uploadfiles/" method="post" enctype="multipart/form-data">
            <input type="file" name="files" multiple>
            <input type="submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)
