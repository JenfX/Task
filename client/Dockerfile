FROM python:3.10
WORKDIR /client
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

RUN apt-get update
RUN apt-get -y install postgresql-client
RUN chmod +x wait-for-postgres.sh

#RUN alembic upgrade head
#CMD [ "python", "main.py" ]
