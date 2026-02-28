from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    value: str

@app.post("/predict")
def predict(data: TextInput):
    text = data.value
    return {"result": text}