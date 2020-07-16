import threading
import socket
import sys
import time



host = '192.168.10.2'
port = 8889
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)


def recv():
    while True:
        try:
            data,server = sock.recvfrom(1024)
            print(data)
        except Exception:
            print("Exiting now. press ctrl+c for full exit")
            break


recvThread = threading.Thread(target=recv)
recvThread.dameon = True
recvThread.start()


while True:
    try:
        msg = input("");
        if not msg:
            break
        if 'end' in msg:
            print ('...')
            sock.close()
            break
        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
