FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    pkg-config \
    libssl-dev

# Upgrade pip, setuptools, and wheel *before* installing anything else
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Try installing with pre-built wheels first
RUN pip install --no-cache-dir  -r requirements.txt

CMD ["hypercorn", "main:app", "--bind", "::"]





