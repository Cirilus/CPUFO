FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN apt update

RUN apt install -y tesseract-ocr tesseract-ocr-rus libglu1-mesa-dev

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app/

RUN export FORCE_CMAKE=1
RUN export CMAKE_ARGS=-DLLAMA_CUBLAS=on

RUN poetry remove llama-cpp-python
RUN  poetry add llama-cpp-python
RUN poetry lock

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]