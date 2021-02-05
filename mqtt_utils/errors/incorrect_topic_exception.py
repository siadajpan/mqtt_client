from mqtt_utils.errors.mqtt_exception import MQTTException


class IncorrectTopicException(MQTTException):
    def __init__(self, message):
        super().__init__(message)
