"""
SQLAlchemy database models.
"""

from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)

from .core import Base


class Product(Base):
    """Product model representing the products table."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    price_category_id = Column(Integer)
    brand_id = Column(String)
    has_image = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)


class ProductEmbedding(Base):
    """Product embedding model representing the product_embeddings table."""

    __tablename__ = "product_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    embeddings = Column(Text)  # JSON string containing the embedding array
    created_at = Column(DateTime, default=datetime.now)


class ProductFeature(Base):
    """Product feature model representing the product_features table."""

    __tablename__ = "product_features"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    feature_name = Column(String, nullable=False)
    feature_value = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class Variant(Base):
    """Variant model representing the variants table."""

    __tablename__ = "variants"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    size_label = Column(String)
    is_one_size = Column(Boolean)
    normalized_size = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
