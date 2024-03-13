#---
# name: transformers-py311
# config: config.py
# group: llm
# depends: [pytorch-py311, torchvision-py311, huggingface_hub-py311, rust-py311]
# test: [test.py, huggingface-benchmark.py]
# docs: docs.md
# notes: bitsandbytes and auto_gptq dependencies added on JetPack5 for 4-bit/8-bit quantization
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG TRANSFORMERS_PACKAGE=transformers
ARG TRANSFORMERS_VERSION=https://pypi.org/pypi/transformers/json

ADD ${TRANSFORMERS_VERSION} /tmp/transformers_version.json

# if you want optimum[exporters,onnxruntime] see the optimum package
RUN python3.11 -m pip install --no-cache-dir --verbose \
	accelerate \
	optimum \
	sentencepiece

# install from pypi, git, ect (sometimes other version got installed)
RUN python3.11 -m pip uninstall -y transformers && \
    python3.11 -m pip install --no-cache-dir --verbose ${TRANSFORMERS_PACKAGE}

# "/usr/local/lib/python3.8/dist-packages/transformers/modeling_utils.py", line 118
# AttributeError: module 'torch.distributed' has no attribute 'is_initialized'
RUN PYTHON_ROOT=`python3.11 -m pip show transformers | grep Location: | cut -d' ' -f2` && \
    sed -i 's|torch.distributed.is_initialized|torch.distributed.is_available|g' -i ${PYTHON_ROOT}/transformers/modeling_utils.py
    
# add benchmark script
COPY huggingface-benchmark.py /usr/local/bin
    
# make sure it loads
RUN python3.11 -m pip show transformers && python3.11 -c 'import transformers; print(transformers.__version__)'