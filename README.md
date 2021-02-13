# mqtt message template
Template to use for mqtt message project

## Requirements
Install requirements using
```bash
pip install -r requirements.txt
```

## MessageManager
Message menager is a thread that waits for the queue from mqtt_client and 
executes messages registered at constructor
If you are using message manager, you don't need to initialize MQTTClient 
anymore.

```python3
from mqtt_utils.message_manager import MessageManager, MQTTMessage

# Define your message that inherit after MQTTMessage
messages = [MQTTMessage('topic')]

# Create message manager. It creates mqtt clients and subscribe to topics from
# messages
message_manager = MessageManager(messages)

# You can update credentials if your broker needs it
message_manager.update_credentials('user', 'password')

# Connect to address and port from broker
message_manager.connect('address', 1234)

# Start the thread
message_manager.start()

# Loop forever (blocking method) -> This calls mqtt client loop_forever
message_manager.loop_forever()

# You need to stop it if loop forever is stopped e.g. by KeyboardInterrupt
message_manager.stop()
```

## MQTTClient example

```python3
from mqtt_utils.mqtt_client import MQTTClient

# define topics to listen to
mqtt_client = MQTTClient()

# if there is a username and password, specify it before connection
mqtt_client.update_username_password('user', 'password')

# All incoming messages will be put into messages queue, 
# make sure to use messages.queue.get() in your code to read them
# Messages will be type MQTTMessage
message_queue = mqtt_client.message_queue

# Connect to the broker with specific address and port
# After connection is established, topics will be registered for listening
mqtt_client.connect('address', 1234)

# Subscribe to topics. You can call this method any time after creating mqtt 
# object. Subscription will happen automatically after connection/reconnection
topics_to_listen = ["topic", "other_topic"]
mqtt_client.subscribe(topics_to_listen)

# You can also unsubscribe from any topics:
mqtt_client.unsubscribe("topic")

# Use this method to publish messages to some topic
publish_method = mqtt_client.publish('other_topic', 'payload')

# Start looping. This function is blocking
mqtt_client.loop_forever()
```
