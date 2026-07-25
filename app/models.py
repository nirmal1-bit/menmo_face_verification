from insightface.app import FaceAnalysis

face_model = FaceAnalysis(
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"]
)

face_model.prepare(ctx_id=0)
