import numpy as np
import threading
import socket
import sys
import time

class DroneFly:
    def __init__(self, no_wifi_test=False):
        if not no_wifi_test:
            self.host = '192.168.10.2'
            self.port = 8889
            self.locaddr = (self.host,self.port)
            self.tello_address = ('192.168.10.1', 8889)

            # Create a UDP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tello_address = ('192.168.10.1', 8889)
            self.sock.bind(self.locaddr)

            # creating a thread that listens to the socket
            recvThread = threading.Thread(target=self.recv)
            recvThread.dameon = True
            recvThread.start()

    def recv(self,):
        while True:
            try:
                data,server = self.sock.recvfrom(1024)
                #print(data, float(data))
                self.data=data
            except Exception:
                print("Exiting now. press ctrl+c for full exit")
                break
    @property
    def return_data(self,):
        return float(self.data)


    def send_command(self,msg):
        msg = msg.encode(encoding="utf-8")
        sent = self.sock.sendto(msg, self.tello_address)


if __name__ == '__main__':
    obj = DroneFly(no_wifi_test= True)
    obj.send_command("command")
    print("sent command sleep and will sleep for 7 seconds")
    time.sleep(7)
    print("sent message takoff")
    obj.send_command("takeoff")
    print("sleep for 7 seconds")
    obj.send_command("land")
    print("landing")
