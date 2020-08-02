import numpy as np
import threading
import socket
import sys
import time

"""
Class that sends and receives messages to the drone
"""


class DroneFly:
    def __init__(self):
        self.host = '192.168.10.2'
        self.port = 8889
        self.locaddr = (self.host,self.port)
        self.tello_address = ('192.168.10.1', 8889)

        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tello_address = ('192.168.10.1', 8889)
        self.sock.bind(self.locaddr)
        self.data = -1

    @property
    def return_data(self):
        """
        returns the data collect from the drone, that is not a standard or
        error messages. Needs to  receives msg to gather the input from
        the drone.
        """
        return self.data

    def send_command(self,msg):
        """
        Sends the msg, specified in the input, to the drone as a String
        through.
        """
        msg_send = msg.encode(encoding="utf-8")
        sent = self.sock.sendto(msg_send, self.tello_address)
        self.msg = msg

    def receive_msg(self,):
        """
        Receives the msgs from the drone.
        If the message is a standard ok message, it is ignored.
        If the message is information about the drone, i.e battery,
        flight time, speed, saves as a variable (self.data).
        If the message is an error message, it prints it in red.
        in order to return the data, use the return_data function
        """
        data, server = self.sock.recvfrom(1024)
        data =data.decode(encoding="utf8")
        try:
            if self.msg == "time?":
                self.data = data
            else:
                #can only float if it's velocity or battery
                self.data = float(data)
        except ValueError:
            #gives a red error message
            if not data == "ok":
                print('\033[31m' + data)
                print('\033[39m')

if __name__ == '__main__':
    #A simple test to
    obj = DroneFly()
    msg = "command"
    obj.send_command(msg)
    obj.receive_msg()
    msg = "time?"
    obj.send_command(msg)
    obj.receive_msg()
    print("time_flight:",obj.return_data)
    msg = "battery?"
    obj.send_command(msg)
    obj.receive_msg()
    print("battery:",obj.return_data)
    msg= "speed?"
    obj.send_command(msg)
    obj.receive_msg()
    print("speed",obj.return_data)
