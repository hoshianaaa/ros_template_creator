# ros_template_creator
## install

```
cd ~/
git clone https://github.com/hoshianaaa/ros_template_creator.git
```

add following code in `~/.bashrc`

```
python_node ()
{
  python3 ~/ros_template_creator/python_node.py $@       
}

launch_template ()
{
  python3 ~/ros_template_creator/launch_template.py $@
}
```



## commands
### python_node

```
cd catkin_ws/src/pkg/scripts
python_node aaa
```

- output `aaa.py`

```python:aaa.py
#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

# start diff
def sd():
  global start
  return now() - start # ex: 0.1 (0.1s)

# last diff
def ld():
  global last
  n = now()
  diff = n - last
  last = n
  return diff

def now():
  return rospy.get_time()

def callback(msg):
  print(msg.data)

rospy.init_node("aaa")
start= now()
last = now()

pub_topic_name = rospy.get_param("~pub", "data")
sub_topic_name = rospy.get_param("~sub", "data")

print("pub:",pub_topic_name)
print("sub:",sub_topic_name)

pub = rospy.Publisher(pub_topic_name, Float64, queue_size=10)
rospy.Subscriber(sub_topic_name, Float64, callback)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  pub.publish(Float64(0))
  print("sd:",sd())
  print("ld:",ld())
  r.sleep()

'''
- example run command
rosrun scripts aaa.py _pub:=aaa _sub:=aaa
'''
```

### launch_template

```
launch_template aaa
```

- output `aaa.launch`

```xml:aaa.luanch
<?xml version="1.0"?>

<launch>

  <!--include file="$(find xxx)/launch/xxx.launch"/-->
  <!--node pkg="xxx" type ="xxx" name="xxx" output="log"/-->
  <!--node pkg="xxx" type ="xxx" name="xxx" output="screen"/-->

</launch>
```

### Convert files to Strings

- how to do

https://qiita.com/hoshianaaa/items/8c6172c1a872494ecd5d

- Tools (`Converting files to Strings`)

https://www.espruino.com/File+Converter

