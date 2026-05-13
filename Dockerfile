FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

CMD ["python", "app.py"]
