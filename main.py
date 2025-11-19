from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from fer.fer import FER
from PIL import Image
import io

app = FastAPI()

# MTCNN consome MUITA RAM → removido
detector = FER()  

@app.post("/analisar-emocao")
async def analisar_emocao(imagem: UploadFile = File(...)):
    try:
        contents = await imagem.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        img_np = np.array(image)

        results = detector.detect_emotions(img_np)

        if not results:
            return JSONResponse({"erro": "Nenhum rosto detectado na imagem."}, status_code=400)

        emotions = results[0]["emotions"]
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
