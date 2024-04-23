FROM python:3.11-alpine

WORKDIR /app

RUN apk update

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt


RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate
RUN pip install torch pyarrow

CMD ["python3", "app.py"]
