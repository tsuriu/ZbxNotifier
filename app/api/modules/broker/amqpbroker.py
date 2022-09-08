from sqlite3 import connect
from loguru import logger
from amqpstorm import Connection, Message, AMQPError
from utils import on_message


class broker:
    def __init__(self, host="localhost", user="guest", password="guest", port=5672, vhost="/"):
        self._host = host
        self._port = port
        self._vhost = vhost
        self._user = user
        self._password = password


    def __connect__(self):
        try:
            conn = Connection(self._host, self._user, self._password, self._port, self._vhost)
        except AMQPError as e:
            conn = None
            logger.error(e)

        return conn


    def sPub(self, queue_name, message):
        with self.__connect__() as conn:
            with conn.channel() as channel:
                channel.queue.declare(queue_name)

                properties = {
                    'content_type': 'text/plain',
                    'headers': {'key': 'value'}
                }

                message = Message.create(channel, message, properties)

                message.publish(queue_name)


    def sConsume(self, queue_name):
        with self.__connect__() as conn:
            with conn.channel() as channel:
                channel.queue.declare(queue_name)

                channel.basic.qos(100)

                channel.basic.consume(on_message, 'simple_queue', no_ack=False)

                try:
                    channel.start_consuming()
                except KeyboardInterrupt:
                    channel.close()