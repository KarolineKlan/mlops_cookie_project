
# Base image
FROM python:3.11-slim

# Install Python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY src/ src/
COPY data/ data/
COPY models/ models/
COPY reports/ reports/


WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

ENTRYPOINT ["python", "-u", "src/mlops_cookie_project1/train.py"]


# # Base image
# FROM python:3.11-slim AS base

# RUN apt update && \
#     apt install --no-install-recommends -y build-essential gcc && \
#     apt clean && rm -rf /var/lib/apt/lists/*


# COPY src src/
# COPY requirements.txt requirements.txt
# COPY requirements_dev.txt requirements_dev.txt
# COPY README.md README.md
# COPY pyproject.toml pyproject.toml


# COPY mlops_cookie_project1/ mlops_cookie_project1/
# COPY data/ data/

# WORKDIR /
# RUN pip install -r requirements.txt --no-cache-dir
# RUN pip install . --no-deps --no-cache-dir

# RUN pip install -r requirements.txt --no-cache-dir --verbose
# RUN pip install . --no-deps --no-cache-dir --verbose

# ENTRYPOINT ["python", "-u", "src/mlops_cookie_project1/train.py"]
