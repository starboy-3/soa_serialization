FROM python:latest

RUN pip install --upgrade pip
RUN pip install protobuf grpcio grpcio-tools
RUN pip install click

COPY test_data.proto .
COPY protobuf_serializer.py .
COPY interface.py .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. test_data.proto
COPY run.py .
CMD ["python", "run.py", "-f", "pbuffer"]