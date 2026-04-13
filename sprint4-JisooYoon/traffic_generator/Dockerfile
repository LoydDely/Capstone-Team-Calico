FROM python:3.11-bullseye

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY simulator.py /app/simulator.py

CMD ["python", "simulator.py"]
