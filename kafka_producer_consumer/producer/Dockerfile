# Base image olarak Python kullan
FROM python:3.9-slim

# Çalışma dizinine geç
WORKDIR /app

# Gerekli sistem paketlerini yükle (mysqlclient için gerekli paketler)
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    pkg-config \
    gcc

# Gerekli dosyaları kopyala
COPY weather_producer.py /app
COPY ../../requirements.txt /app

# pip güncelle
RUN pip install --upgrade pip

# Python bağımlılıklarını yükle
RUN pip install -r requirements.txt

# Uygulamayı başlat
CMD ["python", "weather_producer.py"]
