# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

# Configure server
RUN pip install -r requirements.txt


COPY . /code

## Comment below for local version
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi.application"]

CMD gunicorn STX_Semerjyan.wsgi:application --bind 0.0.0.0:$PORT