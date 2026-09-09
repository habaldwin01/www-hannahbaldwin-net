FROM python:3.14-slim-bookworm

WORKDIR /opt/app
COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /opt/app/src
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"]
