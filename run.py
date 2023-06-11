import argparse
import os
import socket
import string
import sys
import time
import click
import random

r = random.Random()

RANDOM_WORD_SIZE = 10

def generate_data():
     return {
        "id": int(r.random() * 10000),
        "name": randomword(RANDOM_WORD_SIZE),
        "buyers": generate_bids(),
        "year": int(r.random() * 10000),
        "size": r.random() * 10000
    }

def generate_bids():
    bids = {}
    for _ in range(8):
        bids[randomword(10)] = int(r.random() * 10000)
    return bids

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))

def get_serializer(format_name):
    match format_name:
        case 'naive':
            from naive_serializer import NaiveSerializer
            serializer = NaiveSerializer()
        case 'avro':
            from avro_serializer import AvroSerializer
            serializer = AvroSerializer()
        case 'json':
            from json_serializer import JSONSerializer
            serializer = JSONSerializer()
        case 'pbuffer':
            from protobuf_serializer import ProtoSerializer
            serializer = ProtoSerializer()
        case 'mpack':
            from mpack_serializer import MessagePackSerializer
            serializer = MessagePackSerializer()
        case 'yaml':
            from yaml_serializer import YAMLSerializer
            serializer = YAMLSerializer()
        case 'xml':
            from xml_serializer import XMLSerializer
            serializer = XMLSerializer()
    return serializer

FORMATS = [
    "naive",
    "avro",
    "json",
    "pbuffer",
    "mpack",
    "yaml",
    "xml"
]

def main(format):
    data = generate_data()
    serializer = get_serializer(format)
    start_time = time.time()
    serialized_data = serializer.serialize(data)
    serialization_time = time.time() - start_time

    start_time = time.time()
    _ = serializer.deserialize(serialized_data)
    deserialization_time = time.time() - start_time

    return f"""
    {format}
    sizeof - {sys.getsizeof(serialized_data)}
    serialization time: {serialization_time * 1000:.3f}ms
    deserialization time: {deserialization_time * 1000:.3f}ms
    """

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--format', required=True, choices=FORMATS, dest='format_name', help='The format of the data')
    args = parser.parse_args()
    format_name = args.format_name

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', int(os.environ.get(f'SERVER_PORT'))))

    while True:
        request, back = server_socket.recvfrom(1024)
        response = main(format_name)
        server_socket.sendto(response.encode(), back)