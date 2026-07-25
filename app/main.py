import cv2
from fastapi import FastAPI, UploadFile
from fastapi.params import File
import numpy as np
from app.services import get_face_embedding 


app = FastAPI()


@app.get("/")
async def health():
    return {"status": "ok"} 


@app.post("/verify")
async def verify(image: UploadFile = File(...)):
    image_bytes = await image.read()

    # converting bytes to numpy array
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)

    # decoding jpeg/png bytes into an OpenCV image
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Invalid image"}

    result = get_face_embedding(img)

    return {
        "embedding": result.tolist()
    }
