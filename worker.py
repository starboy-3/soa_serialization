import json
import pickle
from abc import abstractmethod, ABC

import msgpack
import yaml
from avro.schema import parse
from avro.io import DatumReader, DatumWriter, BinaryDecoder, BinaryEncoder
from io import BytesIO
from xml_marshaller import xml_marshaller

from google.protobuf.json_format import ParseDict
from test_data_pb2 import MonaLizaPicture

schema = parse("""
{
  "type": "record",
  "name": "MonaLizaPicture",
  "fields": [
    {"name": "id", "type": "int"},
    {"name": "name", "type": "string"},
    {"name": "buyers", "type": {"type": "map", "values": "int"}},
    {"name": "year", "type": "int"},
    {"name": "size", "type": "float"}
  ]
}
""")

class ISerializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserialize(self, obj):
        pass


class AvroSerializer(ISerializer):
    def serialize(self, obj):
        writer = DatumWriter(schema)
        bytes_writer = BytesIO()
        encoder = BinaryEncoder(bytes_writer)
        writer.write(obj, encoder)
        return bytes_writer.getvalue()

    def deserialize(self, obj):
        reader = DatumReader(schema)
        bytes_reader = BytesIO(obj)
        decoder = BinaryDecoder(bytes_reader)
        return reader.read(decoder)

class JSONSerializer(ISerializer):
    def serialize(self, obj):
        return json.dumps(obj)

    def deserialize(self, obj):
        return json.loads(obj)

class MessagePackSerializer(ISerializer):
    def serialize(self, obj):
        return msgpack.packb(obj)

    def deserialize(self, obj):
        return msgpack.unpackb(obj)

class NaiveSerializer(ISerializer):
    def serialize(self, obj):
        return pickle.dumps(obj)

    def deserialize(self, obj):
        return pickle.loads(obj)


class ProtoSerializer(ISerializer):
    def serialize(self, obj):
        scheme = MonaLizaPicture()
        ParseDict(obj, scheme)
        return scheme.SerializeToString()

    def deserialize(self, obj):
        deserialized_obj = MonaLizaPicture()
        deserialized_obj.ParseFromString(obj)
        return deserialized_obj

class YAMLSerializer(ISerializer):
    def serialize(self, obj):
        return yaml.dump(obj)

    def deserialize(self, obj):
        return yaml.load(obj, Loader=yaml.Loader)

class XMLSerializer:
    def serialize(self, obj):
        return xml_marshaller.dumps(obj)

    def deserialize(self, obj):
        return xml_marshaller.loads(obj, )