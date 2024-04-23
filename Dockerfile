FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN apk update && \
    apk add --no-cache gcc python3-dev musl-dev linux-headers

RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate
RUN pip install torch pyarrow

CMD ["python3", "app.py"]
