.PHONY: install test lint validate

install:
	python -m pip install -e '.[dev]'

test:
	pytest

lint:
	ruff check src tests scripts
	ruff format --check src tests scripts
	mypy src

validate:
	python scripts/validate_catalog.py
