import queue
import time
import unittest
from unittest.mock import MagicMock, patch

from mqtt_utils.message_manager import MessageManager
from mqtt_utils.messages.mqtt_message import MQTTMessage


class TestMessageManager(unittest.TestCase):
    def setUp(self) -> None:
        self.messages = []
        self.error_topic = 'error_topic'
        self.message_manager = MessageManager(self.messages,
                                              self.error_topic)
        self.message_manager._mqtt_client = MagicMock()

    @patch('mqtt_utils.messages.utils.payload_from_json')
    def test_execute_message_checks_message_by_topic(self, payload_from_json_mock):
        # given
        self.message_manager._check_message = MagicMock(return_value=None)

        # when
        self.message_manager._execute_message('topic', 'message')

        # then
        self.message_manager._check_message.assert_called()
        payload_from_json_mock.assert_not_called()

    def test_stop_running(self):
        # given
        self.message_manager._execute_message = MagicMock()
        self.message_manager._message_queue = queue.Queue()

        # when
        self.message_manager.start()

        # then
        self.message_manager.stop()
        time.sleep(0.01)
        self.message_manager._execute_message.assert_called_once()

    def test_message_manager_gets_correct_message(self):
        # given
        message1 = MQTTMessage('topic1')
        message1.payload = 'payload1'
        message2 = MQTTMessage('topic2')
        message2.payload = 'payload2'
        messages = [message1, message2]
        self.message_manager._mqtt_client.message_queue = queue.Queue()
        self.message_manager.subscribe_messages(messages)
        self.message_manager._execute_message = MagicMock()

        # when
        self.message_manager.start()
        self.message_manager._message_queue.put(message2)

        # then
        time.sleep(0.01)
        self.message_manager._execute_message.assert_called_with(
            'topic2', 'payload2')
        self.message_manager.stop()
