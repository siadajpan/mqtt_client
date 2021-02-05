import logging
from abc import ABC
from typing import Dict, Any


class MQTTMessage(ABC):
    def __init__(self, topic):
        self.topic = topic
        self.payload = ''
        self._logger = logging.getLogger(self.__class__.__name__)

    def execute(self, payload: Dict[str, Any]):
        raise NotImplementedError()

    def __repr__(self):
        return f'MQTT message with topic: {self.topic}, ' \
               f'payload: {self.payload}'
