import cv2
import numpy as np

from app.model import face_app


def get_face_embedding(image):
    """
    Detect exactly one face and return its embedding.
    """

    faces = face_app.get(image)

    if len(faces) == 0:
        raise ValueError("No face detected.")

    if len(faces) > 1:
        raise ValueError("Multiple faces detected.")



    return faces[0].embedding


def cosine_similarity(vec1, vec2):
    """
    Compute cosine similarity between two vectors.
    """

    dot_product = np.dot(vec1, vec2)

    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    return dot_product / (norm1 * norm2)


# function to call
def verify_faces(image1, image2, threshold=0.5):
    """
    Compare two images.
    """

    embedding1 = get_face_embedding(image1)
    embedding2 = get_face_embedding(image2)

    similarity = cosine_similarity(
        embedding1,
        embedding2,
    )

    return {
        "same": similarity >= threshold,
        "similarity": float(similarity),
    }


