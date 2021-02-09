FROM python:3.6
WORKDIR /opt/project
RUN mkdir -p /opt/project

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["/bin/sh","-c", "python manage.py runserver"]