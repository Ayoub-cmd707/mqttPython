import paho.mqtt.client as mqtt

# Define the MQTT client and connect to the broker
client = mqtt.Client()
client.connect("localhost", 1883)
print("sending message")
# Publish the "Hello World" message on the "hello/world" channel
client.publish("hello/world", "Hello World")