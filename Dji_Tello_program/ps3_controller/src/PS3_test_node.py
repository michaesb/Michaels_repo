import numpy as np
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

"""
Test script that prints the messages from the PS-controller.
"""

def listener(data):
    print(data.axes)
    print(data.buttons)


if __name__ == '__main__':
    try:
        rospy.init_node("JoyPS3")
        rospy.Subscriber("joy",Joy, listener)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
