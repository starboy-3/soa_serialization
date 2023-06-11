import pickle
from interface import ISerializer

class NaiveSerializer(ISerializer):
    def serialize(self, obj):
        return pickle.dumps(obj)

    def deserialize(self, obj):
        return pickle.loads(obj)