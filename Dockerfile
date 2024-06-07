FROM python:3.9-slim-buster

WORKDIR /app

RUN mkdir -p /reports/

COPY report_generator.py /app/

RUN pip install --no-cache-dir requests

CMD ["python", "report_generator.py"]
