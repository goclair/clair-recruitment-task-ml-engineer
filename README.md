# Clair Recruitment Task - ML Engineer

## Part 2: Software Engineering

Deploy your trained model from Part 1 as a FastAPI application for performance prediction.

## Setup

1. Create virtual environment:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   cd src
   uvicorn main:app --reload
   ```

## Task

Implement the prediction endpoint:

**POST /variants/{variant_id}/predict/**
- Accepts `year` and `season` in request body
- Fetches variant data from database
- Uses your trained model to make predictions
- Returns performance score

## Database

SQLite database with normalized tables:
- `products` - Basic product info
- `product_embeddings` - Product embeddings (JSON)
- `product_features` - Product features (key-value pairs)
- `variants` - Product variants
