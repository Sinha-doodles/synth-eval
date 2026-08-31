.PHONY: test lint format serve
test:
	pytest tests -v
lint:
	ruff check .
format:
	ruff format .
serve:
	uvicorn syntheval.api.server:app --reload --port 8000
