# Bibliotecas para instalar:
# pip install fastapi uvicorn numpy opencv-python Pillow fer python-multipart

#	 curl -X POST "http://104.41.50.188:8000/analisar-emocao" \
#     -H "accept: application/json" \
#     -F "imagem=@pessoa_triste.jpg"

# Rodar a API
# uvicorn main:app --host 0.0.0.0 --port 8000


from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from fer.fer import FER
from PIL import Image
import io

app = FastAPI()
detector = FER(mtcnn=True)  # Usa MTCNN para detectar a face

@app.post("/analisar-emocao")
async def analisar_emocao(imagem: UploadFile = File(...)):
    try:
        # Ler bytes da imagem
        contents = await imagem.read()

        # Converter para array
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        img_np = np.array(image)

        # Detectar emoções
        results = detector.detect_emotions(img_np)

        if not results:
            return JSONResponse({"erro": "Nenhum rosto detectado na imagem."}, status_code=400)

        # Pega a primeira face detectada
        emotions = results[0]["emotions"]

        # Emoção predominante
        dominante = max(emotions, key=emotions.get)

        return {
            "emocao_predominante": dominante,
            "porcentagens": emotions
        }

    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)


@app.get("/")
def root():
    return {"status": "API de reconhecimento facial rodando!"}
