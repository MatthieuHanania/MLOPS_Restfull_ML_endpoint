# Dockerfile to build a flask app

FROM python:3.9
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY mnistModel.h5 .
COPY fashion-mnist_test.csv .
EXPOSE 5000
CMD ["python","app.py"]
