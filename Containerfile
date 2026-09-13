FROM python:3.14-slim-bookworm

WORKDIR /opt/app
COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/app/requirements.txt
COPY ./src /opt/app/src
WORKDIR /opt/app/src
# net.ipv6.bindv6only=1
# CMD ["gunicorn", "--bind", "[::]:8080", "--bind", "0.0.0.0:8080", "main:app"]
# net.ipv6.bindv6only=0
CMD ["gunicorn", "--bind", "[::]:8080", "main:app"]


