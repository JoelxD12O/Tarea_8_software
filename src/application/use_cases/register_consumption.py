from src.domain.entities.consumption import Consumption
from src.domain.ports.message_broker import MessageBrokerPort

class RegisterConsumptionUseCase:
    def __init__(self, broker: MessageBrokerPort):
        self.broker = broker

    def execute(self, consumption: Consumption) -> None:
        # En una arquitectura hexagonal, el caso de uso se encarga de la lógica de aplicación
        # En este caso, publicar el evento al broker
        self.broker.publish_consumption(consumption)
