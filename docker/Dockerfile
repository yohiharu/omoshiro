FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip

COPY ./app /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt --break-system-packages

CMD ["python3", "main.py"]
