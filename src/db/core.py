"""
Core database configuration and utilities.
"""

import os
from collections.abc import Generator
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


# Database URL - use absolute path to ensure consistent location
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'products_and_variants.db')}"

# Create engine
engine = create_engine(DATABASE_URL, echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables() -> None:
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """Dependency to get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables on module import
create_tables()


def test_connection() -> dict[str, Any]:
    """Test database connection and return basic info."""
    try:
        db = SessionLocal()
        # Import here to avoid circular imports
        from .tables import Product, Variant

        product_count = db.query(Product).count()
        variant_count = db.query(Variant).count()
        db.close()
        return {
            "status": "connected",
            "product_count": product_count,
            "variant_count": variant_count,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
