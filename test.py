import cv2

from app.model import face_app


image = cv2.imread("./images/2.jpeg")

if image is None:
    raise ValueError("Could not load image.")


faces = face_app.get(image)

for face in faces:
    # bounding Box
    x1, y1, x2, y2 = face.bbox.astype(int)

    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2,
    )

    # detection Confidence
    confidence = f"{face.det_score:.2f}"

    cv2.putText(
        image,
        confidence,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )

    # facial Landmarks
    for point in face.landmark_2d_106:
        x, y = point.astype(int)

        cv2.circle(
            image,
            (x, y),
            1,
            (0, 0, 255),
            -1,
        )


cv2.imshow("Face Detection", image)

cv2.waitKey(0)

cv2.destroyAllWindows()



