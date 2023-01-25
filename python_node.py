import sys
import os

import os

# https://softhints.com/python-change-directory-parent/
def getud_name():
  return os.path.abspath(os.curdir)

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

string1 = '#!/usr/bin/env python\n\nimport rospy\nfrom std_msgs.msg import *\nfrom geometry_msgs.msg import *\n\n# start diff\ndef sd():\n  global start\n  return now() - start # ex: 0.1 (0.1s)\n\n# last diff\ndef ld():\n  global last\n  n = now()\n  diff = n - last\n  last = n\n  return diff\n\ndef now():\n  return rospy.get_time()\n\ndef callback(msg):\n  print(msg.data)\n\nrospy.init_node(\"'

string2 = "\")\nstart= now()\nlast = now()\n\npub_topic_name = rospy.get_param(\"~pub\", \"data\")\nsub_topic_name = rospy.get_param(\"~sub\", \"data\")\n\npub = rospy.Publisher(pub_topic_name, Float64, queue_size=10)\nrospy.Subscriber(sub_topic_name, Float64, callback)\n\nr = rospy.Rate(10)\n\nwhile not rospy.is_shutdown():\n  pub.publish(Float64(0))\n  print(\"sd:\",sd())\n  print(\"ld:\",ld())\n  r.sleep()\n\n'''\n- example run command\nrosrun "

string3 = ".py _pub:=aaa _sub:=aaa\n'''\n"

pkg_name = getud_name()

string = string1 + node_name + string2 + pkg_name + " " + node_name + string3

with open(path, 'a') as f:
  print(string, file=f)

os.system("sudo -A chmod +x " + path)
