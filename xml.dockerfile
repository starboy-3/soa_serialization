FROM python:latest

RUN pip install --upgrade pip
RUN pip install xml_marshaller
RUN pip install click
COPY run.py .
COPY xml_serializer.py .
COPY interface.py .

CMD ["python", "run.py", "-f", "xml"]