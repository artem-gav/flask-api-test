FROM python:2.7

COPY ./requirements.txt /app/
RUN chmod 664 /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]