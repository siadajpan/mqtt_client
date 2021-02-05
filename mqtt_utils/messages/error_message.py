from mqtt_utils.messages.mqtt_message import MQTTMessage


class ErrorMessage(MQTTMessage):
    def __init__(self, topic: str):
        super().__init__(topic)

    def execute(self, payload):
        pass
