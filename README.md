# mqtt_client
Client for mqtt connection

# Requirements
Install requirements using
```bash
pip install -r requirements.txt
```

# Run

```python3
from mqtt_client.mqtt_client import MQTTClient

# define topics to listen to
mqtt_client = MQTTClient()

# if there is a username and password, specify it before connection
mqtt_client.update_username_password('user', 'password')

# All incoming messages will be put into message queue, 
# make sure to use message.queue.get() in your code to read them
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

# Use this method to publish message to some topic
publish_method = mqtt_client.publish('other_topic', 'payload')

# Start looping. This function is blocking
mqtt_client.loop_forever()
```