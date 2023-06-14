FROM python:3.10

WORKDIR /marco

COPY . /marco/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
