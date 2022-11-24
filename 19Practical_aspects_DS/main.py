
# https://fastapi.tiangolo.com/
from typing import Union
from typing import List

from pydantic import BaseModel

from fastapi import FastAPI, Request

from joblib import dump, load

app = FastAPI()


class Prediction(BaseModel):
    """Prediction class"""
    prediction: int

# whenever you go to the root of the website, it will return this


@app.get("/predict", response_model=Prediction)
def read_root(req: Request):
    sepallength = req.query_params["sepallength"]
    sepalwidth = req.query_params["sepalwidth"]
    petallength = req.query_params["petallength"]
    petalwidth = req.query_params["petalwidth"]

# http://127.0.0.1:8000/predict?sepallength=0.2&sepalwidth=0.2&petallength=0.2&petalwidth=0.2

    sample = [sepalwidth, sepallength, petalwidth, petallength]
    model = load(
        "E:/Project/dsr32/19Practical_aspects_DS/iris_pipeline.joblib")
    prediction = model.predict([sample])

    return {"prediction": str(prediction[0])}

# print(3+2)
