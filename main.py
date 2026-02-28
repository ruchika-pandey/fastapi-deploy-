from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ML Inference API")

class InputData(BaseModel):
    value: float

@app.get("/")
def home():
    return {"message": "FastAPI ML Inference API Running"}

@app.post("/predict")
def predict(data: InputData):
    prediction = data.value * 2   # Dummy ML logic
    return {"prediction": prediction}