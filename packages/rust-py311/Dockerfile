#---
# name: rust-py311
# group: build
# depends: [build-essential, python3.11]
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustc --version && \
    python3.11 -m pip install --no-cache-dir --verbose setuptools-rust
