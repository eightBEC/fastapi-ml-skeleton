from pydantic import BaseModel


class HousePredictionResult(BaseModel):
    median_house_value: int
    currency: str = "USD"
