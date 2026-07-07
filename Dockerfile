FROM python:3.11-slim
WORKDIR /app
COPY Requirements.txt .
RUN pip install -r Requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
