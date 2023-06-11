from avro.schema import parse
from avro.io import DatumReader, DatumWriter, BinaryDecoder, BinaryEncoder
from io import BytesIO
from interface import ISerializer

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
