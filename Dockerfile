FROM python:3.13-slim
WORKDIR /app
COPY requierements.txt .
RUN pip install --no-cache-dir -r requierements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
