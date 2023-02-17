#!/usr/bin/python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



class object_irritation_robot:

    def __init__(self):
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    


if __name__ == '__main__':
    rospy.init_node('object_irritation_robot', anonymous=True)
    object_irritation_robot()
    rospy.spin()