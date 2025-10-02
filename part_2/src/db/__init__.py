"""
Database module for the product performance prediction API.
"""

from .core import SessionLocal, create_tables, engine, get_db, test_connection
from .queries import get_product_by_id
from .tables import Product, ProductEmbedding, ProductFeature, Variant

__all__ = [
    "engine",
    "SessionLocal",
    "get_db",
    "create_tables",
    "test_connection",
    "Product",
    "ProductEmbedding",
    "ProductFeature",
    "Variant",
    "get_product_by_id",
]
