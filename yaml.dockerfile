FROM python:latest

RUN pip install --upgrade pip
RUN pip install pyyaml
RUN pip install click
COPY run.py .
COPY yaml_serializer.py .
COPY interface.py .
CMD ["python", "run.py", "-f", "yaml"]