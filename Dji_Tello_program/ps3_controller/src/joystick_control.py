import numpy as np
import rospy
import time, sys
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from drone_class import DroneFly

"""
A class that takes input PS-controller from the joynode
and sends command to the drone through the wifi
"""


class CommandCentral:
    def _init__(self):
        self.data_prev = (-1) #tuple with the commands from the joystick

        # storing variables to compare to the new input
        self.L_axis_prev = np.zeros(4)
        self.L_axis_new = np.zeros(4)
        self.R_axis_prev = np.array(4)
        self.R_axis_new = np.array(4)

        # starting the drone msgs
        #self.obj_drone_fly = Dronefly()
        #self.obj_drone_fly.send_command("command")

        #status
        self.battery = -1
        self.speed = -1
        self.time_flight = -1

    def receive_msg(self,data):
        #logging a full tuple of the information
        print("test start")
        print(data.buttons)
        print(data.axes)
        print("test finish")
        self.data_prev = data.axes + data.buttons
        #checking for axis data in the controller

        if not data.axes[:] == (0,0,1,0,0,1):
            print (data.axes,type(data.axes))
            if not data.axes[0] == 0 and not data.axes[1] ==0:
                self.move_drone(data.axes[0],data.axes[1])
        #checking buttons
        if data.buttons[0]: # x-button
            self.go_down()
        if data.buttons[2]: # triangle-button
            self.go_up()
        if data.buttons[9]: # start button
            self.status_drone()

    #Simple movement

    def go_up(self,):
        print("go_up")

    def go_down(self):
        print("go down")

    def steer_in_the_plane(self):
        print("steer_in_the_plane")

    def status_drone(self,):
        """
        self.obj_drone_fly.send_command("battery?")
        self.battery= self.obj_drone_fly.return_data
        self.obj_drone_fly.send_command("speed?")
        self.speed= self.obj_drone_fly.return_data
        self.obj_drone_fly.send_command("time?")
        self.time_flight = self.obj_drone_fly.return_data
        """
        battery = self.battery
        print("battery at", self.battery, ";speed at", self.speed,\
              ";time at", self.time_flight,";",end= "\r")

if __name__ == '__main__':
    obj = CommandCentral()

    obj.status_drone()
    time.sleep(1)
    obj.status_drone()
    exit()
    try:
        rospy.init_node("CommandCentral")
        rospy.Subscriber("joy",Joy, obj.receive_msg)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
