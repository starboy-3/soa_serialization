FROM python:latest

RUN pip install --upgrade pip
RUN pip install avro
RUN pip install click
COPY run.py .
COPY interface.py .
COPY avro_serializer.py .

CMD ["python", "run.py", "-f", "avro"]