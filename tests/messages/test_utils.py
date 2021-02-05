import json
from unittest import TestCase
from unittest.mock import patch

from mqtt_utils.errors.incorrect_payload_exception import \
    IncorrectPayloadException
from mqtt_utils.messages import utils


class UtilsTest(TestCase):
    def test_payload_from_json_returns_None_if_no_message(self):
        # given
        message = None

        # when
        result = utils.payload_from_json(message)

        # then
        self.assertIsNone(result)

    @patch('json.loads')
    def test_payload_from_json_raises_incorrect_payload_exception(
            self, patch_loads):
        # given
        message = 'some_message'
        patch_loads.side_effect = ValueError()

        # when
        self.assertRaises(IncorrectPayloadException, utils.payload_from_json, message)

    def test_payload_from_json_makes_dict_from_json(self):
        # given
        message = json.dumps({'foo': 'bar'})

        # when
        result = utils.payload_from_json(message)

        # then
        self.assertIsInstance(result, dict)
