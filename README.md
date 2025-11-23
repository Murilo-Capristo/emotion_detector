# EMMA Emotion Detector - API de Reconhecimento Facial

Bem-vindo ao repositório da **API de Reconhecimento Facial** do projeto EMMA! Esta API é responsável por analisar expressões faciais dos usuários e inferir seu estado emocional, integrando-se ao aplicativo EMMA para registrar o humor de forma automática.

---

## Funcionalidades

- Recebe imagens do rosto do usuário enviadas por um curl.
- Analisa expressões faciais usando **modelos de reconhecimento de emoções (FER - Facial Expression Recognition)**.
- Retorna a emoção detectada (feliz, triste, neutro, surpreso, raiva, medo, nojo) com probabilidade associada.

---

## Como Funciona no App

1. O usuário tira uma foto ou envia um vídeo curto de seu rosto pelo app EMMA, ou por meio de um curl.
2. O app envia a imagem para esta API.
3. A API processa a imagem e detecta a emoção predominante usando o modelo FER.
4. O resultado é enviado de volta ao app e salvo no banco de dados junto com timestamp.

---

## Tecnologias Utilizadas

- Python 
- FastAPI para criar endpoints REST
- Bibliotecas de reconhecimento facial: `fer`, `opencv`, `tensorflow` ou equivalentes

---

## Endpoints

- `POST /analisar-emocao`  
  Envia uma imagem do rosto e retorna a emoção detectada.
  
---

## Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Murilo-Capristo/emotion_detector.git

   cd emotion_detector

2. Instale as dependências:
   ```bash
   pip install fastapi uvicorn numpy opencv-python Pillow fer python-multipart

3. Rode a API localmente:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000

4. Teste, enviando uma imagem no curl (você precisa está dentro da pasta da imagem, e depois realizar o curl):
   ```bash
   	 curl -X POST "http://localhost:8000/analisar-emocao" \
     -H "accept: application/json" \
     -F "imagem=@pessoa_triste.jpg"
     ```
     Ou na aplicação real, sem precisar rodar localmente:
      ```bash
     	 curl -X POST "http://104.41.50.188:8000/analisar-emocao" \
     -H "accept: application/json" \
     -F "imagem=@pessoa_triste.jpg"

