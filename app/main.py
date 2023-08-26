from fastapi import FastAPI
from pydantic import BaseModel
from app.modelsandvectorizer.pred import pred_pipeline

app = FastAPI()

class TextIn(BaseModel):
    title: str
    body: str



@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/predict")
def predict(text: TextIn):
    label = pred_pipeline(text.body, text.title)
    return {"tag": label}



