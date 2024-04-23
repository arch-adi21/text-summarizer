FROM python:3.9-alpine

WORKDIR /app

RUN apk update

COPY . /app/
RUN pip install -r requirements.txt


RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
