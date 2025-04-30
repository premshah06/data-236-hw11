from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model at startup
model = joblib.load("model.pkl")
app = FastAPI()

# Define input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width:  float
    petal_length: float
    petal_width:  float

@app.post("/predict")
def predict(i: IrisInput):
    features = [[i.sepal_length, i.sepal_width, i.petal_length, i.petal_width]]
    pred = int(model.predict(features)[0])
    return {"prediction": pred}
