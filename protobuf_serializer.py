from google.protobuf.json_format import ParseDict
from test_data_pb2 import MonaLizaPicture

class ProtoSerializer(ISerializer):
    def serialize(self, obj):
        scheme = MonaLizaPicture()
        ParseDict(obj, scheme)
        return scheme.SerializeToString()

    def deserialize(self, obj):
        deserialized_obj = MonaLizaPicture()
        deserialized_obj.ParseFromString(obj)
        return deserialized_obj
