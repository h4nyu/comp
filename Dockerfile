FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        python3-minimal \
        python3-pip \
    && ln -s /usr/bin/python3.10 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* \
    # && pip install --no-cache-dir torch torchvision --extra-index-url https://download.pytorch.org/whl/cu118
# RUN ln -s /usr/local/cuda/lib64/libnvrtc.so.11.2 /usr/local/cuda/lib64/libnvrtc.so

WORKDIR /app
COPY . .
