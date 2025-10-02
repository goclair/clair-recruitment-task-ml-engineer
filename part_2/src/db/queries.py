"""
TODO: Implement required database queries here.
"""

from sqlalchemy.orm import Session

from .tables import Product


def get_product_by_id(db: Session, product_id: int) -> Product:
    """
    Fetch product data by ID.

    Args:
        db: Database session
        product_id: Product ID to fetch

    Returns:
        Product data

    Raises:
        ValueError: If product is not found
    """
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise ValueError(f"Product {product_id} not found")

    return product
