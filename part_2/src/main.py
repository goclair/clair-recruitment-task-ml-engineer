"""
FastAPI application for product performance prediction.
This is a stub implementation for the recruitment task.
"""

from db import get_db, get_product_by_id
from fastapi import Depends, FastAPI
from models import PredictionRequest, PredictionResponse, ProductResponse
from sqlalchemy.orm import Session

app = FastAPI(
    title="Product Performance Prediction API",
    description="API for predicting product performance",
    version="1.0.0",
)


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int, db: Session = Depends(get_db)
) -> ProductResponse:
    """Get product information by ID."""
    product = get_product_by_id(db, product_id)
    return ProductResponse.model_validate(product)


@app.post("/variants/{variant_id}/predict/", response_model=PredictionResponse)
async def predict_performance(
    variant_id: int, request: PredictionRequest, db: Session = Depends(get_db)
) -> PredictionResponse:
    """
    TODO: Implement this endpoint.
    """
    raise NotImplementedError("Not implemented")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
