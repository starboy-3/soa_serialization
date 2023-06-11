from xml_marshaller import xml_marshaller
from interface import ISerializer

class XMLSerializer(ISerializer):
    def serialize(self, obj):
        return xml_marshaller.dumps(obj)

    def deserialize(self, obj):
        return xml_marshaller.loads(obj, )