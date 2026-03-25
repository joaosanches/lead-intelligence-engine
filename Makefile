.PHONY: setup test run smoke validate

UV_CACHE_DIR ?= /tmp/uv-cache

setup:
	UV_CACHE_DIR=$(UV_CACHE_DIR) uv sync --group dev

test:
	UV_CACHE_DIR=$(UV_CACHE_DIR) PYTHONPATH=. uv run pytest -q

run:
	UV_CACHE_DIR=$(UV_CACHE_DIR) uv run uvicorn app.main:app --reload

smoke:
	UV_CACHE_DIR=$(UV_CACHE_DIR) LLM_PROVIDER=mock PYTHONPATH=. uv run python scripts/smoke_test.py

validate: test smoke
