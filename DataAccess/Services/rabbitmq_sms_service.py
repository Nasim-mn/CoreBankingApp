import json
import os

import pika

from Common.Services.isms_service import ISmsService


class RabbitMQSmsService(ISmsService):
    # Same names as the teacher's consumer (main.py) so both sides match.
    EXCHANGE = "notification-exchange"
    QUEUE = "notification-queue"
    ROUTING_KEY = "notification"

    def __init__(self):
        # Values come from .env; defaults match the teacher's example.
        self.host = os.getenv("RABBITMQ_HOST", "localhost")
        self.port = int(os.getenv("RABBITMQ_PORT", "5672"))
        self.virtual_host = os.getenv("RABBITMQ_VHOST", "/")
        self.username = os.getenv("RABBITMQ_USERNAME", "guest")
        self.password = os.getenv("RABBITMQ_PASSWORD", "guest")

    def send(self, phone: str, content: str) -> bool:
        connection = None
        try:
            parameters = pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                virtual_host=self.virtual_host,
                credentials=pika.PlainCredentials(self.username, self.password),
                connection_attempts=1,
                socket_timeout=3,  # don't freeze the UI for long if RabbitMQ is down
            )
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            channel.exchange_declare(exchange=self.EXCHANGE, exchange_type="direct", durable=True)
            channel.queue_declare(queue=self.QUEUE, durable=True)
            channel.queue_bind(queue=self.QUEUE, exchange=self.EXCHANGE, routing_key=self.ROUTING_KEY)

            channel.confirm_delivery()

            body = json.dumps({"phone": phone, "content": content}).encode()
            channel.basic_publish(
                exchange=self.EXCHANGE,
                routing_key=self.ROUTING_KEY,
                body=body,
                properties=pika.BasicProperties(content_type="application/json", delivery_mode=2),
                mandatory=True,
            )
            return True
        except Exception as ex:
            print(f"SMS publish failed -> {ex}")
            return False
        finally:
            if connection is not None and connection.is_open:
                connection.close()