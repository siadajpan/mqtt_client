import json
import logging
from typing import Any, Dict, Optional

from mqtt_utils.errors.incorrect_payload_exception import \
    IncorrectPayloadException

logger = logging.getLogger('MqttUtils')


def payload_from_json(message: Optional[str]) -> Optional[Dict[str, Any]]:
    if not message:
        return None

    try:
        logger.debug(f'Loading message into dict {message}')
        message_dict = json.loads(message)
        logger.debug(f'Message loaded {message_dict}')
        return message_dict
    except Exception as ex:
        error_message = f'Received a message that is not json: {message}, {ex}'
        logger.error(error_message)
        raise IncorrectPayloadException(error_message)
