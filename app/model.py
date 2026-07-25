from insightface.app import FaceAnalysis


face_app = FaceAnalysis(
    providers=["CPUExecutionProvider"]
)

face_app.prepare(
    ctx_id=0,
)

# resizing the mage to 640px * 640px for less computation overhead 
