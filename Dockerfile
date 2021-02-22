FROM python:3.7
WORKDIR /opt/project
RUN mkdir -p /opt/project

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python3", "manage.py", "runserver", "0.0.0.0:9000"]
