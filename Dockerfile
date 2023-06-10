FROM ubuntu:22.04

WORKDIR /service
COPY . .
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN pip install --upgrade pip
RUN pip install protobuf grpcio grpcio-tools
RUN pip install msgpack
RUN pip install xml_marshaller
RUN pip install avro
RUN pip install click
RUN pip install pyyaml
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. test_data.proto

#ENTRYPOINT [ "python", "run.py", "--file", "NAIVE"]