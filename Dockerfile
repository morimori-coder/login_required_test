# # FROM python:3.11-slim
FROM python:3.11

RUN apt-get update

WORKDIR /workspace
COPY ./requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt
