FROM python:latest

RUN pip install --upgrade pip

RUN pip install click
COPY interface.py .
COPY run.py .
COPY interface.py .
COPY json_serializer.py .
CMD ["python", "run.py", "-f", "json"]