import queue
import pika
from loguru import logger


class broker:
    def __init__(self, host="localhost", port=5627, vhost="/", username="guest", password="guest"):
        self._host = host
        self._port = port
        self._vhost = vhost
        self._user = username
        self._password = password

        self._channel = self.__channel__()


    def __credentials__(self):
        try:
            credentials = pika.PlainCredentials(self._user, self._password)
        except Exception as e:
            credentials = None
            logger.error(e)
        
        return credentials


    def __params__(self):
        try:
            params = pika.ConnectionParameters(self._host, self._port, self._vhost, self.__credentials__())
        except Exception as e:
            params = None
            logger.error(e)

        return params


    def __connection__(self):
        try:
            conn = pika.BlockingConnection(parameters=self.__params__())            
        except Exception as e:
            conn = None
            logger.error(e)

        return conn


    def __channel__(self):
        try:
            channel = self.__connection__.channel()
        except Exception as e:
            channel = None
            logger.error(e)
        
        return channel


    def __close__(self):
        try:
            self.__connection__.close()
        except Exception as e:
            logger.error(e)


    def __declare__(self, descr, type, ex_type=None):
        try:
            if type in ["q", "queue"]:
                self._channel.queue_declare(queue=descr)
            if type in ["ex", "exchange"]:
                self._channel.exchange_declare(exchange=descr, exchange_type=ex_type)
        except Exception as e:
            logger.error(e)


    def publisher(self):
        pass

    def consumer(self):
        pass