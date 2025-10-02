from pydantic import BaseModel


class PredictionRequest(BaseModel):
    year: int
    season: str


class PredictionResponse(BaseModel):
    variant_id: int
    year: int
    season: str
    performance: float
