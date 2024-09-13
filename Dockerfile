FROM python:3.10

ENV PYTHONUNBUFFERED=1

# RUN mkdir /test_docker
WORKDIR /test_docker

COPY . /test_docker
COPY requirements.txt /test_docker

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /test_docker

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
