import socket
import time


"""
simple UDP-script to test and understand.
Sends messages to the other software
"""

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
counter = 0
string_msgs = "hello world"
while True:
    counter+=1
    sock.sendto(string_msgs[0:counter].encode(),(UDP_IP, UDP_PORT))
    time.sleep(1)
    if len(string_msgs)< counter:
        print("full_message")
        break
