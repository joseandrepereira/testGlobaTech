FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Instalar o cliente PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client
COPY . .

EXPOSE 8000
CMD ["./wait-for-db.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]
