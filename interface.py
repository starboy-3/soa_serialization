from abc import abstractmethod, ABC

class ISerializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass

    @abstractmethod
    def deserialize(self, obj):
        pass