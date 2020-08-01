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
        #tuples with commands
        self.data_prev = (-1) #tuple with the commands from the joystick
        self.data_buttons_prev = (-1)
        self.data_axes_prev = (-1)
        # storing variables to compare to the new input
        self.L_axis_prev = np.zeros(4)
        self.L_axis_new = np.zeros(4)
        self.R_axis_prev = np.array(4)
        self.R_axis_new = np.array(4)

        # starting the drone msgs
        self.obj_drone_fly = DroneFly()
        self.obj_drone_fly.send_command("command")
        self.obj_drone_fly.receive_msg()

        #status
        self.battery = -1
        self.speed = -1
        self.time_flight = -1

        #threading
        self.continue_thread_msg = [0]
        recvThread = threading.Thread(target=self.thread_send_msg())
        recvThread.dameon = True


    def receive_msg(self,data):
        #stops the thread when you receive a new message
        self.data = data
        if self.continue_thread_msg[0]:
            self.continue_thread_msg[0] = False
        #takeoff and landing
        if data.buttons[4] and data.buttons[5]:
            #self.drone_takoff() # drone takeoff
            pass
        if data.axes[2] == -1 and data.axes[5]==-1:
            self.drone_land() # drone land

        if abs(data.axes[0])==1 or abs(data.axes[1])==1:
            self.steer_in_the_plane(data.axes[0],data.axes[1])

        if data.axes[0] or data.axes[1] or data.axes[3] or data.axes[4]:
            if
            self.continue_thread_msg[0] = True
            recvThread = threading.Thread(target=self.thread_send_msg())
            recvThread.dameon = True
            recvThread.start()

        #stopping the thread (or at least try)
        if sum(data.buttons)==0:
            print("turning thing to false")
            self.continue_thread_msg[0] = False

        if data.buttons != self.data_buttons_prev:
            #steering
            if data.buttons[0]: # x-button
                self.go_down() # go downwards
            if data.buttons[2]: # triangle-button
                self.go_up() # go upwards
            if data.buttons[1]: # circle-button
                self.rotate_cw() #rotate clockwise
            if data.buttons[3]: # square-button
                self.rotate_ccw() #rotate counterclockwise

            if data.buttons[9]: # start button
                self.status_drone() #checking status

            #additional steering
            if data.buttons[13]: #arrow up
                self.go_forward()
            if data.buttons[14]: #arrow down
                self.go_back()
            if data.buttons[15]: #arrow left
                self.go_left()
            if data.buttons[16]: #arrow right
                self.go_right()
        #logging a full tuple of the information
        self.data_prev = data.axes + data.buttons
        self.data_axes_prev = data.axes
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
        print("go_up")
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

    def thread_send_msg(self):
        counter = 0
        while self.continue_thread_msg[0]:
            print(self.data.axes[:],str(counter))
            time.sleep(0.95)
            counter +=1


    def steer_in_the_plane(self,y,x):
        print("steer_in_the_plane")

    def status_drone(self,):
        #getting battery status
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
