FROM mcr.microsoft.com/vscode/devcontainers/anaconda:dev-3

ARG conda_env=algo_trading

RUN conda create -n algo_trading python=3.6.9
ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env
# Activate the environment, and make sure it's activated:
# Make RUN commands use the new environment:
# SHELL ["conda", "run", "-n", "algo_trading", "/bin/bash", "-c"]
RUN conda info --envs
RUN python --version
# do zipline install manually
RUN conda install -n algo_trading -c conda-forge zipline
RUN conda install -n algo_trading -c conda-forge pyfolio
# Theano dependencies
RUN conda install -n algo_trading mkl-service 
# g++ and friends
RUN conda install -c msys2 m2w64-toolchain
# install other packages
RUN conda install jupyter matplotlib
# install yahoofinancials for python3.8
RUN python3.8 -m pip install yahoofinancials
# Dont need to copy environment files over
COPY scripts/extension.py  .
RUN mkdir -p ~/.zipline && cp extension.py ~/.zipline/extension.py
# ingest does not work in zipline
# RUN zipline ingest -b quantopian-quandl
ENTRYPOINT [ "/bin/bash" ]