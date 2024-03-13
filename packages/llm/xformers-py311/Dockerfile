#---
# name: xformers-py311
# group: llm
# config: config.py
# depends: [pytorch-py311:distributed]
# requires: '>=34.1.0'
# test: test.py
# notes: https://github.com/facebookresearch/xformers
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG TORCH_CUDA_ARCH_LIST

# https://github.com/facebookresearch/xformers/blob/main/docs/source/custom_parts/index.rst#triton-parts
# could not find a version that satisfies the requirement triton
#RUN pip3 install --no-cache-dir --verbose triton

# force rebuild on new releases
ADD https://pypi.org/pypi/xformers/json /tmp/xformers_version.json

RUN python3.11 -m pip list && python3.11 -c 'import setuptools'

# install from pip
RUN MAX_JOBS=8 python3.11 -m pip install --no-cache-dir --verbose 'xformers!=0.0.21'
RUN python3.11 -m pip install --force-reinstall --no-cache-dir --verbose /opt/torch*.whl

ENV XFORMERS_MORE_DETAILS=1
RUN python3.11 -m pip show xformers && python3.11 -c 'import xformers.info; xformers.info.print_info()'
