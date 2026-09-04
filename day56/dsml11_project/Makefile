help:
	@echo
	@echo "install: Install dependencies using uv"
	@echo "dev : Run the FastAPI develpoment server"
	@echo "lint: Run code liniting using ruff"
	@echo "mypy: Run type checking using mypy"
	@echo "format: Format code using ruff"
	@echo

.PHONY: install
install:
	uv sync --frozen

.PHONY: dev
dev:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: mypy
mypy:
	uv run mypy .

.PHONY: format
format:
	uv run ruff check --fix .
	uv run ruff format .
