from typing import Callable

from fastapi import FastAPI


def preload_model() -> None:
    """
    In order to load model on memory to each worker
    """
    from services.predict import MachineLearningModelHandlerScore

    MachineLearningModelHandlerScore.get_model()


def create_start_app_handler(app: FastAPI) -> Callable[..., None]:
    def start_app() -> None:
        preload_model()

    return start_app
