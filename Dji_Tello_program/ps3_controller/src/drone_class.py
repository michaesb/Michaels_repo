import numpy as np
import threading
import socket
import sys
import time

class DroneFly:
    def __init__(self, no_wifi_test=False):
        self.host = '192.168.10.2'
        self.port = 8889
        self.locaddr = (self.host,self.port)
        self.tello_address = ('192.168.10.1', 8889)

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tello_address = ('192.168.10.1', 8889)
        self.sock.bind(self.locaddr)
        self.data = -1
        self.battery= -1
        self.speed = -1


    @property
    def return_data(self,):
        return self.data


    def send_command(self,msg):
        msg_send = msg.encode(encoding="utf-8")
        sent = self.sock.sendto(msg_send, self.tello_address)
        self.msg = msg

    def receive_msg(self,):
        try:
            data, server = self.sock.recvfrom(1024)
            data =data.decode(encoding="utf8")
            if self.msg == "time?":
                self.data = data
            else:
                self.data = float(data)
            #print(self.msg,self.data)
        except ValueError:
            if not data == "ok":
                print('\033[31m' + data)
                print('\033[39m')

if __name__ == '__main__':
    obj = DroneFly()
    msg = "command"
    obj.send_command(msg)
    obj.receive_msg()
    msg = "battery?"
    obj.send_command(msg)
    obj.receive_msg()
    obj.return_data
    msg= "speed?"
    obj.send_command(msg)
    obj.receive_msg()
    obj.return_data
