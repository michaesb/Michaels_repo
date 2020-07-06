import numpy as np
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

"""
varaible stores is not saved in a good way here. Need to look into send by
reference perhaps?
"""

def listener(data):
    print("hello world")
    print(data.axes[:])


if __name__ == '__main__':
    try:
        rospy.init_node("JoyPS3")
        rospy.Subscriber("joy",Joy, listener)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
