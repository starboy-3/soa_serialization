FROM python:latest

RUN pip install --upgrade pip
RUN pip install click
COPY run.py .
COPY interface.py .
COPY naive_serializer.py .

CMD ["python", "run.py", "-f", "naive"]