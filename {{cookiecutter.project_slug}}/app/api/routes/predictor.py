from typing import Any

import joblib
from core.errors import PredictException
from fastapi import APIRouter, HTTPException
from core.logging import getLogger
from models.prediction import HealthResponse, MachineLearningResponse
from services.predict import MachineLearningModelHandlerScore as model

router = APIRouter()

logger = getLogger(__name__)

def get_prediction(data_input: Any = None) -> MachineLearningResponse:
    return MachineLearningResponse(
        model.predict(data_input, load_wrapper=joblib.load, method="predict_proba")
    )


@router.get("/predict", response_model=MachineLearningResponse, name="predict:get-data")
async def predict(data_input: Any = None) -> MachineLearningResponse:
    if not data_input:
        raise HTTPException(status_code=404, detail=f"'data_input' argument invalid!")
    try:
        prediction = get_prediction(data_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception: {e}")

    return MachineLearningResponse(prediction=prediction)


@router.get(
    "/health", response_model=HealthResponse, name="health:get-data",
)
async def health() -> HealthResponse:
    is_health = False
    try:
        get_prediction("lorem ipsum")
        is_health = True
        return HealthResponse(status=is_health)
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")