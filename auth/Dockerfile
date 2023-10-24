
FROM python

ENV FILESYSTEM_ROOT=$FILESYSTEM_ROOT

WORKDIR $FILESYSTEM_ROOT

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY users.json ./
COPY app.py ./

# CMD ["flask","run"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]