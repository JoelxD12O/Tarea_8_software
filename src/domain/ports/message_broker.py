from abc import ABC, abstractmethod
from src.domain.entities.consumption import Consumption

class MessageBrokerPort(ABC):
    @abstractmethod
    def publish_consumption(self, consumption: Consumption) -> None:
        pass

    @abstractmethod
    def start_consuming(self, callback) -> None:
        pass
