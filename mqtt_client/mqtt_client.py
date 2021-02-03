import logging
from queue import Queue
from typing import Optional, List

import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(
            client_id="", clean_session=True, userdata=None,
            protocol=mqtt.MQTTv311, transport="tcp")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.logger = logging.getLogger(self.__class__.__name__)
        self.message_queue = Queue()
        self.registered_topics = []

    def update_username_password(self, username: str, password: str):
        self.client.username_pw_set(username=username, password=password)

    def connect(self, address: str, port: int):
        self.logger.info(f'MQTT client connecting to address: {address}'
                         f'port: {port}')

        self.client.connect(address, port)

    def loop_forever(self):
        self.logger.info('MQTT client looping start')
        self.client.loop_forever()

    def subscribe(self, topics: List[str]) -> None:
        """
        Subscribe to additional topics
        :param topics:
        :return:
        """
        for topic in topics:
            if topic in self.registered_topics:
                continue

            self.registered_topics.append(topic)
            self.client.subscribe(topic)

    def unsubscribe(self, topics: List[str]) -> None:
        """
        Unsubscribe from topics
        :param topics:
        :return:
        """
        for topic in topics:
            if topic not in self.registered_topics:
                continue

            self.registered_topics.remove(topic)
            self.client.unsubscribe(topic)

    def on_connect(self, client, userdata, flags, rc):
        """
        Subscribe to registered topics. This function is automatically called
        on connection
        :param client:
        :param userdata:
        :param flags:
        :param rc:
        :return:
        """
        self.logger.info(f'MQTT connected')
        for topic in self.registered_topics:
            self.logger.info(f'Subscribing to {topic}')
            self.client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        """
        This function is run every time client receives a message.
        Message is put on the message queue. It's up to application running
        MQTTClient to get this message from queue
        :param client:
        :param userdata:
        :param msg:
        :return:
        """
        self.logger.info(f'Message received topic: '
                         f'{msg.topic}, payload: {msg.payload}')
        self.message_queue.put(msg)

    def publish(self, topic: str, payload: Optional[str]):
        """
        Publish message to topic.
        :param topic:
        :param payload:
        :raises: Exception when publishing topic raised one
        :return:
        """
        self.logger.info(f'Publishing message topic: {topic}, '
                         f'payload: {payload}')
        try:
            self.client.publish(topic, payload)
        except Exception as ex:
            self.logger.error(ex)
            raise ex
