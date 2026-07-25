from insightface.app import FaceAnalysis


face_app = FaceAnalysis(
    providers=["CPUExecutionProvider"]
)

face_app.prepare(
    ctx_id=0,
    det_size=(640, 640),
)

# resizing the mage to 640px * 640px for less computation overhead 
