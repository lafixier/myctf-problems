FROM python:3.10.7-slim-buster

RUN mkdir /var/www
WORKDIR /var/www

COPY app .
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8002", "app:app"]
