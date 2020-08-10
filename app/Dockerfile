FROM python:3.6.1-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

CMD ["python","app.py"]
