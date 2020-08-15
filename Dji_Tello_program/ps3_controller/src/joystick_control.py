import numpy as np
import rospy
import time, sys
import threading
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from drone_class import DroneFly

"""
A class that takes input PS-controller from the joynode
and sends command to the drone through the wifi
"""


class CommandCentral:
    def __init__(self):
        #tuples with all the input from the controller
        self.data_buttons_prev = (-1)

        # starting the drone msgs
        self.obj_drone_fly = DroneFly()
        self.obj_drone_fly.send_command("command")
        self.obj_drone_fly.receive_msg()

        #determining the type of controller
        self.PS_version = -2

        #status
        self.battery = -1
        self.speed = -1
        self.time_flight = -1

    def receive_msg(self,data):
        """
        A function that triggers when it receives a message from the playstation
        controller. Here it translates the tuples into the correct buttons and
        use this information to fly and gather input from the drone.
        """

        #checking the type of controller
        if len(data.axes)==6:
            self.PS_version=3
        elif len(data.axes)==8:
            self.PS_version=4
        else:
            #printing error message
            print('\033[31m')
            print("error in the ps-controller message")
            print('\033[39m')


        #assigning buttons from the buttons
        x, circle, triangle, square = \
        data.buttons[0], data.buttons[1], data.buttons[2], data.buttons[3]


        L_1, R_1, L_2, R_2  = \
        data.buttons[4], data.buttons[5],data.axes[2], data.axes[5]
        Select_Share, Start_Options = \
        data.buttons[8], data.buttons[9]

        #Because of the differences in format between PS3 and PS4 the
        #information is extracted diffently here.
        if self.PS_version ==3:
            arrow_up, arrow_down, arrow_left, arrow_right =\
            data.buttons[13], data.buttons[14], data.buttons[15], data.buttons[16]

        elif self.PS_version ==4:
            arrow_up, arrow_down, arrow_left, arrow_right =0,0,0,0
            if data.axes[6]==1:
                arrow_left=1
            elif data.axes[6]==-1:
                arrow_right=1
            if data.axes[7]==1:
                arrow_up =1
            elif data.axes[7]==-1:
                arrow_down = 1
        else:
            #printing an error message
            print('\033[31m')
            print("error in the ps-controller message")
            print('\033[39m')



        if data.buttons != self.data_buttons_prev:
            #takeoff and landing
            if L_1 and R_1:
                self.drone_takoff()
            #Added extra help to the PS3-controller as it sometimes has trouble
            #getting R_2 and L_2 button to work fully
            if self.PS_version==3:
                if data.buttons[6] and data.buttons[7]:
                    self.drone_land()
            if L_2==-1 and R_2==-1:
                self.drone_land()
            if Select_Share:
                self.do_a_flip()

            #steering
            if x:
                self.go_down()
            if triangle:
                self.go_up()
            if circle:
                self.rotate_cw() #rotate clockwise
            if square:
                self.rotate_ccw() #rotate counterclockwise

            if Start_Options: # start button
                self.status_drone() #checking status


            #additional steering
            if arrow_up:
                self.go_forward()
            if arrow_down:
                self.go_back()
            if arrow_left:
                self.go_left()
            if arrow_right:
                self.go_right()

        #adding the new message as the previous message
        if self.PS_version==4:
            extra_buttons = (arrow_up,arrow_down,arrow_left,arrow_right)
            self.data_buttons_prev= data.buttons+ extra_buttons
        else:
            self.data_buttons_prev = data.buttons

    def drone_takoff(self,):
        print("takeoff")
        self.obj_drone_fly.send_command("takeoff")
        self.obj_drone_fly.receive_msg()

    def drone_land(self,):
        print("land")
        self.obj_drone_fly.send_command("land")
        self.obj_drone_fly.receive_msg()
    #Simple movement
    def go_up(self,):
        print("go upwards")
        self.obj_drone_fly.send_command("up 20")
        self.obj_drone_fly.receive_msg()

    def go_down(self):
        print("go down")
        self.obj_drone_fly.send_command("down 20")
        self.obj_drone_fly.receive_msg()

    def go_forward(self):
        print("forward")
        self.obj_drone_fly.send_command("forward 20")
        self.obj_drone_fly.receive_msg()

    def go_back(self):
        print("backward")
        self.obj_drone_fly.send_command("back 20")
        self.obj_drone_fly.receive_msg()

    def go_right(self):
        print("right-direction")
        self.obj_drone_fly.send_command("right 20")
        self.obj_drone_fly.receive_msg()

    def go_left(self):
        print("left")
        self.obj_drone_fly.send_command("left 20")
        self.obj_drone_fly.receive_msg()

    def rotate_cw(self):
        print("rotate clockwise")
        self.obj_drone_fly.send_command("cw 15")
        self.obj_drone_fly.receive_msg()

    def rotate_ccw(self):
        print("rotate counter clockwise")
        self.obj_drone_fly.send_command("ccw 15")
        self.obj_drone_fly.receive_msg()

    def do_a_flip(self):
        print("flip")
        self.obj_drone_fly.send_command("flip f")
        self.obj_drone_fly.receive_msg()

    def status_drone(self,):
        #getting battery, speed and flight time printed by pressing start/options
        self.obj_drone_fly.send_command("battery?")
        self.obj_drone_fly.receive_msg()
        self.battery= self.obj_drone_fly.return_data
        #getting speed status
        self.obj_drone_fly.send_command("speed?")
        self.obj_drone_fly.receive_msg()
        self.speed= self.obj_drone_fly.return_data
        #getting time status
        self.obj_drone_fly.send_command("time?")
        self.obj_drone_fly.receive_msg()
        self.time_flight = self.obj_drone_fly.return_data
        print("battery:", self.battery,"% ;speed:", self.speed,\
              "cm/s;flight time:", self.time_flight,)

if __name__ == '__main__':
    obj = CommandCentral()
    try:
        rospy.init_node("CommandCentral")
        rospy.Subscriber("joy",Joy, obj.receive_msg)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
