.PHONY: install check format type-check test clean

# Install dependencies
install:
	pip install -r requirements.txt

# Run all linting tools
check: format type-check

# Format code with black and ruff
format:
	black src/
	ruff check --fix src/

# Type checking with mypy
type-check:
	mypy src/

# Run tests (placeholder for future test implementation)
test:
	echo "Tests not implemented yet"

# Clean up cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
