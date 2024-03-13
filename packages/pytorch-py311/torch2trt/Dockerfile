#---
# name: torch2trt-py311
# group: pytorch-py311
# config: config.py
# depends: [pytorch-py311, torchvision-py311]
# test: test.py
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG CUDA_ARCHITECTURES

RUN cd /opt && \
    git clone --depth=1 https://github.com/NVIDIA-AI-IOT/torch2trt && \
    cd torch2trt && \
    python3.11 -m pip install --verbose . && \
    sed 's|^set(CUDA_ARCHITECTURES.*|#|g' -i CMakeLists.txt && \
    cmake -B build -DCUDA_ARCHITECTURES=${CUDA_ARCHITECTURES} . && \
    cmake --build build --target install && \
    ldconfig

RUN python3.11 -m pip show torch2trt && python3.11 -c 'import torch2trt'
