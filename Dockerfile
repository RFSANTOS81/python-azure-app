FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["sh", "-c", "uvicorn main:app --host 127.0.0.1 --port ${PORT:-8000}"]
