FROM python:3.12-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

COPY . .

CMD ["uv", "run", "main.py"]