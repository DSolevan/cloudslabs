FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    git \
    vim \
    nano \
    htop \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --break-system-packages Flask requests numpy pandas


EXPOSE 5000

USER root

CMD ["python3", "app.py"]
