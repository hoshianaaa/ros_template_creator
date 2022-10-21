import sys
args = sys.argv
arg1 = args[1]

path = None
node_name = None
extension = ".py"

if (extension in arg1):
  split_string = arg1.split(".")
  node_name = split_string[0]
  path = arg1
else:
  node_name = arg1
  path = arg1 + extension

string1 = '#!/usr/bin/env python\n\nimport rospy\nfrom std_msgs.msg import *\nfrom geometry_msgs.msg import *\n\ndef callback(msg):\n  print(msg.data)\n\nrospy.init_node("'

string2 = '")\npub = rospy.Publisher("~data", Float64, queue_size=10)\nrospy.Subscriber("~data", Float64, callback)\n\nr = rospy.Rate(10)\n\nwhile not rospy.is_shutdown():\n  pub.publish(Float64(0))\n  r.sleep()'

string = string1 + node_name + string2

with open(path, 'a') as f:
  print(string, file=f)
