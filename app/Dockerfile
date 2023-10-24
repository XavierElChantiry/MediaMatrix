FROM python:3

ENV MYSQL_HOSTNAME="localhost"
ENV MYSQL_PORT=3306
ENV MYSQL_USER="Bobbeh"
ENV MYSQL_PASSWORD="Password"
ENV MYSQL_DATABASE="video"
ENV FILE_SYSTEM_HOSTNAME="localhost"
ENV FILE_SYSTEM_PORT="5001"
ENV PROD="True"

WORKDIR /usr
COPY . ./src

WORKDIR /usr/src

EXPOSE 5003:5000
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]