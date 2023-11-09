FROM python:latest

RUN apt-get update 

WORKDIR /app 

COPY app.py . 

RUN pip install redis
RUN pip install flask 

EXPOSE 80 

CMD ["python", "app.py"]