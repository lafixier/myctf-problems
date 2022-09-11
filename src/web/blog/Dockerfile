FROM python:3.9.2-alpine

RUN mkdir /var/www
WORKDIR /var/www

COPY app .
RUN pip install -r requirements.txt

CMD ["python3", "./app.py"]
