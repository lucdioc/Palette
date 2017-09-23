from network import LoRa
import socket
import binascii
import struct

lora = LoRa(mode=LoRa.LORAWAN)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# make the socket non-blocking
s.setblocking(False)

# get any data received...
while True:
	data = s.recv(256)
	print(data)




	

