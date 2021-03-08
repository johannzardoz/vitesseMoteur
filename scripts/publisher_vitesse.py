#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import UInt16

def talker():
    pub = rospy.Publisher('speed', UInt16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        speed = int(input('speed : '))
        rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass