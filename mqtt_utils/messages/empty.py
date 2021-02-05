from mqtt_utils.messages.mqtt_message import MQTTMessage


class Empty(MQTTMessage):
    def __init__(self):
        super().__init__('Empty')

    def execute(self, payload):
        pass
