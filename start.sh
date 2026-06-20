#!/bin/sh
# Seed fake data on every startup (perfect for ephemeral demo environments)
python seed.py

# Render sets PORT; fallback to 8000 for local Docker
uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
