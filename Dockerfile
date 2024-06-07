FROM python:3.9-slim

WORKDIR /app

COPY generate_report.py .

RUN pip install requests

RUN mkdir -p /reports

CMD ["python", "generate_report.py"]
