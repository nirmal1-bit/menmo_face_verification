import cv2

from app.model import face_app



image = cv2.imread("./images/olivia.avif")

if image is None:
    raise RuntimeError("Failed to load image")



faces = face_app.get(image)

face = faces[0]

print(face.bbox)
print(face.det_score)
print(face.embedding.shape)
