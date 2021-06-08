FROM python:3.7.6

COPY ./requirements.txt /app/requirements.txt
COPY ./app/app.py /app/app.py
WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
