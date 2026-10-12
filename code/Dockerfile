# syntax=docker/dockerfile:1

# ---- Builder stage ----
FROM python:3.12-slim AS builder

# Copy uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /app

# Install dependencies first (cached unless lockfile/pyproject change)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Copy source and install the project itself
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev


# ---- Runtime stage ----
FROM python:3.12-slim AS runtime

# Non-root user
RUN useradd --create-home --uid 1000 app

WORKDIR /app

# Bring in the virtualenv and app code from the builder
COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER app

EXPOSE 8000

# Replace with your actual entrypoint
CMD ["python", "-m", "your_package"]
# e.g. CMD ["uvicorn", "your_package.main:app", "--host", "0.0.0.0", "--port", "8000"]