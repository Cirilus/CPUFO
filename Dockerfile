FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/



RUN apt-get update && apt-get install -y software-properties-common && \
    wget https://developer.download.nvidia.com/compute/cuda/12.3.1/local_installers/cuda-repo-debian12-12-3-local_12.3.1-545.23.08-1_amd64.deb && \
    dpkg -i cuda-repo-debian12-12-3-local_12.3.1-545.23.08-1_amd64.deb && \
    cp /var/cuda-repo-debian12-12-3-local/cuda-*-keyring.gpg /usr/share/keyrings/ && \
    add-apt-repository contrib && \
    apt-get update && \
    apt-get -y install cuda-toolkit-12-3

RUN apt install -y tesseract-ocr tesseract-ocr-rus libglu1-mesa-dev

sudo apt install -y gcc-11 g++-11

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN export FORCE_CMAKE=1
RUN export CMAKE_ARGS=-DLLAMA_CUBLAS=on

RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all-major" FORCE_CMAKE=1 pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]