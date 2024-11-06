# Django va FastAPI uchun umumiy Dockerfile
FROM python:3.11

WORKDIR /app

# Kutubxonalarni o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani nusxalash
COPY . .

# Portlarni ochish
EXPOSE 8000 8001
