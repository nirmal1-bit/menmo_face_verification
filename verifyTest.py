import cv2
import numpy as np

from app.services import verify_faces

from app.model import face_app

image1 = cv2.imread("./images/e2.jpeg")
image2 = cv2.imread("./images/haland.jpeg")

if image1 is None:
    raise ValueError("Could not load person1.jpg")

if image2 is None:
    raise ValueError("Could not load person2.jpg")


result = verify_faces(
    image1,
    image2,
)

print(result)



face1 = face_app.get(image1)[0]
face2 = face_app.get(image2)[0]

print("Embedding shape:", face1.embedding.shape)
print("Norm 1:", np.linalg.norm(face1.embedding))
print("Norm 2:", np.linalg.norm(face2.embedding))

print("Normalized norm 1:", np.linalg.norm(face1.normed_embedding))
print("Normalized norm 2:", np.linalg.norm(face2.normed_embedding))

print(
    "Dot(normalized):",
    np.dot(face1.normed_embedding, face2.normed_embedding),
)

print(
    "Cosine(raw):",
    np.dot(face1.embedding, face2.embedding)
    / (
        np.linalg.norm(face1.embedding)
        * np.linalg.norm(face2.embedding)
    ),
)
