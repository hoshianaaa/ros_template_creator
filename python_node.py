import sys
import os

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))

from python_utils import *

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

string1 = "#!/usr/bin/env python\n\nimport rospy\nfrom std_msgs.msg import *\nfrom geometry_msgs.msg import *\n\nimport os,sys\nsys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))\nsys.path.append(os.path.join(os.path.dirname(__file__), './python_ros_utils'))\n\nfrom python_utils import *\nfrom python_ros_utils import *\n\ndef callback(msg):\n  print(msg.data)\n\nrospy.init_node(\""

string2 = "\")\n\npub_topic_name = rospy.get_param(\"~pub\", \"data\")\nsub_topic_name = rospy.get_param(\"~sub\", \"data\")\n\nprint(\"pub:\",pub_topic_name)\nprint(\"sub:\",sub_topic_name)\n\npub = rospy.Publisher(pub_topic_name, Float64, queue_size=10)\nrospy.Subscriber(sub_topic_name, Float64, callback)\n\nr = rospy.Rate(10)\n\nwhile not rospy.is_shutdown():\n  pub.publish(Float64(0))\n  r.sleep()\n\n'''\n- example run command\nrosrun "

string3 = ".py _pub:=aaa _sub:=aaa\n'''\n"

pkg_name = getud_name()

string = string1 + node_name + string2 + pkg_name + " " + node_name + string3

with open(path, 'a') as f:
  print(string, file=f)

os.system("sudo -A chmod +x " + path)
if isdir("python_ros_utils") is False:
  bash_cmd("git clone git@github.com:hoshianaaa/python_ros_utils.git")

if isdir("python_utils") is False:
  bash_cmd("git clone git@github.com:hoshianaaa/python_utils.git")
