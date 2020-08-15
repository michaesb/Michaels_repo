import socket

"""
simple UDP-script to test and understand.
Receives messages from the other software
"""

UDP_IP = "127.0.0.1" #local adress on the computer
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
    print ("received message:", data)
