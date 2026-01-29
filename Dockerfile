FROM python:3.10-slim

RUN pip install pandas pyarrow

WORKDIR /app

COPY pipeline/pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]

