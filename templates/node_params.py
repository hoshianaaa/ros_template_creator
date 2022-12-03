#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

data = 0.0

###########################################

initial_param = {'param1': 0.0}
param = {'param1': 0.0}

import json
import os

def read_json_file(file_name):
  if os.path.exists(file_name):
    with open(file_name, 'r') as f:
      json_load = json.load(f)
      return json_load, True
  return None, False

def write_json_file(file_name, dict_data):
  with open(file_name, 'w') as f:
    json.dump(dict_data, f, indent=2)

def initialize_file():
  global initial_param
  global f_name
  write_json_file(f_name, initial_param)

def update_file():
  global param
  global f_name
  write_json_file(f_name, initial_param)
###########################################

def callback(msg):
  global data
  data = msg.data
  print("callback",data)

  #########################
  param['param1'] = data 
  update_file()
  ########################

node_name = "aaa"
rospy.init_node(node_name)
f_name = os.environ['HOME'] + "/.ros/" + node_name + "-params.json"
pub = rospy.Publisher("~output", Float64, queue_size=10)
rospy.Subscriber("~input", Float64, callback)

##########################################
file_data, read_sucess = read_json_file(f_name)
if read_sucess == False:
  initialize_file()
else:
  try:
    data = file_data['param1']
    print(data)
  except:
    initialize_file()
##########################################

r = rospy.Rate(10)

while not rospy.is_shutdown():
  pub.publish(Float64(data))
  print("publish",data)
  r.sleep()
