import paho.mqtt.client as mqtt

# Define the MQTT client and connect to the broker
client = mqtt.Client()
client.connect("localhost", 1883)

# Define a callback function that will be called when a message is received on the "hello/world" channel
def on_message(client, userdata, msg):
    print(msg.payload)

# Subscribe to the "hello/world" channel and set the callback function
client.subscribe("hello/world")
client.on_message = on_message

# Start the MQTT client loop
client.loop_forever()
