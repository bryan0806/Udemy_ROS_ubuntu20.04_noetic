#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def callback(data):
    global counter , cup
    counter = counter + 1

    if(counter==3):
        cup = cup + 1
        rospy.loginfo("Cup # %s is ready after mixing %s",cup, data.data)
        counter = 0

    
def listener():
    rospy.init_node('cup', anonymous=True)
    rospy.Subscriber("ingredients", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    counter = 0
    cup = 0
    listener()
