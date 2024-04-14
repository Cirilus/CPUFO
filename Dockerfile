FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/

RUN apt update

RUN apt install -y tesseract-ocr tesseract-ocr-rus libglu1-mesa-dev

RUN pip install -r --no-cache-dir requirements.txt

COPY . /app/

RUN export FORCE_CMAKE=1
RUN export CMAKE_ARGS=-DLLAMA_CUBLAS=on

RUN pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]