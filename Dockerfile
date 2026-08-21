FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app.py ./
COPY models/ ./models/
COPY controllers/ ./controllers/
COPY views/ ./views/
RUN mkdir -p /app/uploads

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "flask", "--app", "app:create_app", "run", "--host", "0.0.0.0", "--port", "8000"]
