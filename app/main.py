from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.append("../")
sys.path.append("../../")

from app.model.model import predict

app = FastAPI()

class TextIn(BaseModel):
    text: str

@app.get("/")
def index():
    return {"message": "Server is up and running"}

@app.post("/predict")
def predict_2(textinput: TextIn):
    prediction = predict(textinput.text)
    return {"prediction of language": prediction}

# if __name__ == "__main__":
#     import uvicorn
#     # run the app with uvicorn on localhost:8000
#     uvicorn.run(app, host="localhost", port=8000)