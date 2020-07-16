import threading
import socket
import sys
import time


host = '192.168.10.2'
port = 8999
locaddr = (host,port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)
msg = sys.argv[1:]

msg = msg[0].encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address)

print("finished")


# def recv():
#     count = 0
#     while True:
#         try:
#             data, server = sock.recvfrom(1518)
#             print(data.decode(encoding="utf-8"))
#         except Exception:
#             print ('\nExit . . .\n')
#             break

#recvThread create
# recvThread = threading.Thread(target=recv)
# recvThread.start()
