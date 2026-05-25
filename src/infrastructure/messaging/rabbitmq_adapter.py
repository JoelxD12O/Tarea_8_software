import pika
import json
from datetime import datetime
from src.domain.entities.consumption import Consumption
from src.domain.ports.message_broker import MessageBrokerPort

class RabbitMQAdapter(MessageBrokerPort):
    def __init__(self, host, port, user, password, virtual_host="/"):
        self.credentials = pika.PlainCredentials(user, password)
        self.parameters = pika.ConnectionParameters(host, port, virtual_host, self.credentials)
        self.queue_name = "recompensas_cola"

    def publish_consumption(self, consumption: Consumption) -> None:
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)
        
        message = {
            "amount": consumption.amount,
            "card_number": consumption.card_number,
            "restaurant_id": consumption.restaurant_id,
            "timestamp": consumption.timestamp.isoformat()
        }
        
        channel.basic_publish(
            exchange="",
            routing_key=self.queue_name,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()

    def start_consuming(self, callback_func) -> None:
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)

        def internal_callback(ch, method, properties, body):
            data = json.loads(body)
            consumption = Consumption(
                amount=data["amount"],
                card_number=data["card_number"],
                restaurant_id=data["restaurant_id"],
                timestamp=datetime.fromisoformat(data["timestamp"])
            )
            callback_func(consumption)

        channel.basic_consume(queue=self.queue_name, on_message_callback=internal_callback, auto_ack=True)
        print(f"[*] Esperando mensajes en {self.queue_name}...")
        channel.start_consuming()
