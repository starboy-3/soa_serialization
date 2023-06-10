import string
import sys
import time
import click
import random
from worker import *


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

MAPPING = {
    "naive": NaiveSerializer(),
    "avro": AvroSerializer(),
    "json": JSONSerializer(),
    "pbuffer": ProtoSerializer(),
    "mpack": MessagePackSerializer(),
    "yaml": YAMLSerializer(),
    "xml": XMLSerializer()
}


@click.command()
@click.option('--format', '-f', required=True, type=click.Choice(MAPPING.keys()))
def main(format):
    data = generate_data()
    serializer = MAPPING.get(format)
    start_time = time.time()
    serialized_data = serializer.serialize(data)
    serialization_time = time.time() - start_time

    start_time = time.time()
    _ = serializer.deserialize(serialized_data)
    deserialization_time = time.time() - start_time

    print(f"{format} - sizeof: {sys.getsizeof(serialized_data)}; serialization time: {serialization_time * 1000:.3f}ms deserialization time: {deserialization_time * 1000:.3f}ms")

if __name__ == '__main__':
    main()