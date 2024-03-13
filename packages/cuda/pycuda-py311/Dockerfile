#---
# name: pycuda-py311
# group: cuda
# config: config.py
# depends: [cuda, build-essential, python3.11, numpy-py311]
# test: test.py
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

#ENV PATH="/usr/local/cuda/bin:${PATH}"
#ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
#RUN echo "$PATH" && echo "$LD_LIBRARY_PATH"

ARG PYCUDA_VERSION

RUN cd /opt && \
    git clone --branch=${PYCUDA_VERSION} --depth=1 --recursive https://github.com/inducer/pycuda && \
    cd pycuda && \
    python3.11 setup.py --verbose build_ext --inplace bdist_wheel && \
    cp dist/pycuda*.whl /opt && \
    rm -rf /opt/pycuda
    
RUN pip3.11 install --no-cache-dir --verbose /opt/pycuda*.whl

# this was needed at some point?
#RUN pip3.11 install --no-cache-dir --verbose six

# make sure it loads
RUN pip3.11 show pycuda && python3.11 -c 'import pycuda; print(pycuda.VERSION_TEXT)'
