from datetime import datetime

from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    category_id: int | None
    price_category_id: int | None
    brand_id: str | None
    has_image: bool | None
    created_at: datetime | None

    class Config:
        from_attributes = True
