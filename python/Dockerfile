FROM python:3.10-slim

WORKDIR /app
COPY /requirements.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

COPY listFiles.py /app/listFiles.py

ENTRYPOINT ["python3", "listFiles.py"]