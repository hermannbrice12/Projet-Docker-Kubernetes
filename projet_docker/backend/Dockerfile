FROM python:latest

WORKDIR /app
RUN apt-get update && upgrade

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

