import json
from interface import ISerializer

class JSONSerializer(ISerializer):
    def serialize(self, obj):
        return json.dumps(obj)

    def deserialize(self, obj):
        return json.loads(obj)