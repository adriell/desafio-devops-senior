FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN apk update && apk upgrade 
RUN apk add --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev make gcc	
RUN pip install --upgrade setuptools 
RUN pip install --upgrade -r requirements.txt
EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi