import zmq

# Create a ZeroMQ context
context = zmq.Context()

# Create a ZeroMQ REQ socket and connect to the subscriber node
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send the "Hello World" message
socket.send("Hello World")