FROM python:3.13-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock* ./

RUN pip install --no-cache-dir --upgrade pip build && \
    pip install --no-cache-dir .

COPY . .

CMD ["uv", "run", "main.py"]