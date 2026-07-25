from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Health": "Working"}



@app.post("/verifyFace")
async def verifyFace():
    







