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
python_node aaa
```

- output `aaa.py`

```python:aaa.py
#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

def callback(msg):
  print(msg.data)

rospy.init_node("aaa")
pub = rospy.Publisher("~data", Float64, queue_size=10)
rospy.Subscriber("~data", Float64, callback)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  pub.publish(Float64(0))
  r.sleep()

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

