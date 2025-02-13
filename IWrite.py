from abc import ABC ,abstractmethod

class IWrite(ABC):
    @abstractmethod
    def Write(self, data: str):
        pass