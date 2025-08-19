FROM continuumio/miniconda3

WORKDIR /src/cads-common

COPY environment.yml /src/cads-common/

RUN conda install -c conda-forge gcc python=3.12 \
    && conda env update -n base -f environment.yml

COPY . /src/cads-common

RUN pip install --no-deps -e .
