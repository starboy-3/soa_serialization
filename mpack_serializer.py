import msgpack
from interface import ISerializer

class MessagePackSerializer(ISerializer):
    def serialize(self, obj):
        return msgpack.packb(obj)

    def deserialize(self, obj):
        return msgpack.unpackb(obj)