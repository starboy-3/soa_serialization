import yaml
from interface import ISerializer

class YAMLSerializer(ISerializer):
    def serialize(self, obj):
        return yaml.dump(obj)

    def deserialize(self, obj):
        return yaml.load(obj, Loader=yaml.Loader)