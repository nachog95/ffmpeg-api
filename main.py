from fastapi import FastAPI, File, UploadFile
import subprocess
import os

app = FastAPI()

@app.post("/compress-audio/")
async def compress_audio(file: UploadFile = File(...)):
    input_file = f"/tmp/input_{file.filename}"
    output_file = f"/tmp/compressed_{file.filename}"

    # Guardar el archivo temporalmente
    with open(input_file, "wb") as buffer:
        buffer.write(await file.read())

    # Comprimir el audio con FFmpeg
    command = ["ffmpeg", "-i", input_file, "-b:a", "64k", output_file]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Leer el archivo comprimido y devolverlo
    with open(output_file, "rb") as f:
        compressed_audio = f.read()

    # Limpiar archivos temporales
    os.remove(input_file)
    os.remove(output_file)

    return {"filename": file.filename, "data": compressed_audio}
