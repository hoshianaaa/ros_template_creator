#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

def callback(msg):
  print(msg.data)

rospy.init_node("xyz")
pub = rospy.Publisher("~data", Float64, queue_size=10)
rospy.Subscriber("~data", Float64, callback)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  pub.publish(Float64(0))
  r.sleep()
