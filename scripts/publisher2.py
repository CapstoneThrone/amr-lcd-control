#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('lcdscreen2', float32, queue_size=10)
    rospy.init_node('sample_publisher2', anonymous=True)

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():

       # test = "test2"
	num = 17
        rospy.loginfo(num)
        pub.publish(num)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#for more on python publishers, wiki.ros.org
