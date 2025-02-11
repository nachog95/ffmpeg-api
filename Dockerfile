# Usa una imagen base que ya incluya FFmpeg
FROM jrottenberg/ffmpeg:latest

# Instala Python y dependencias
RUN apt-get update && apt-get install -y python3 python3-pip

# Copia los archivos de la API
WORKDIR /app
COPY . .

# Instala las dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Comando de inicio para Render
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
