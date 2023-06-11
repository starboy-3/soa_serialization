FROM python:latest

RUN pip install --upgrade pip
RUN pip install msgpack
RUN pip install click
COPY run.py .
COPY interface.py .
COPY mpack_serializer.py .

CMD ["python", "run.py", "-f", "mpack"]