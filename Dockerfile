FROM python:3.9-slim-bullseye

RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /opt/app/app && \
    useradd -m -r appuser && \
    chown appuser /opt/app/

WORKDIR /opt/app

COPY requirements.txt .

COPY app/ app/

RUN pip install -r requirements.txt

USER appuser

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
