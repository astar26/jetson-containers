#---
# name: python3.11
# alias: python3.11
# group: build
# depends: build-essential
# notes: installs core python3.11 packages and pip
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND=noninteractive

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
    apt-get install -y --no-install-recommends \
		  python3.11-dev \
		  python3.11-pip \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean
    
RUN which pip3 && pip3.11 --version && \
    python3.11 -m pip install --upgrade pip

# this was causing issues downstream (e.g. Python2.7 still around in Ubuntu 18.04,
# and in cmake python enumeration where some packages expect that 'python' is 2.7)
#RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \
#    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
    
RUN which python || python --version || pip --version || \
    which python3.11 || python3.11 --version || pip3.11 --version

RUN pip3.11 install --upgrade --no-cache-dir \
	setuptools \
	packaging \
	'Cython<3' \
	wheel
	
RUN pip3.11 install --no-cache-dir --verbose wget psutil
