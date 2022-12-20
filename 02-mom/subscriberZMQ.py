import zmq

# Create a ZeroMQ context
context = zmq.Context()

# Create a ZeroMQ REP socket and bind to a port
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Receive the message and print it
message = socket.recv()
print(message)