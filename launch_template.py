import sys
args = sys.argv
arg1 = args[1]

path = None
node_name = None
extension = ".launch"

if (extension in arg1):
  split_string = arg1.split(".")
  node_name = split_string[0]
  path = arg1
else:
  node_name = arg1
  path = arg1 + extension

data = open("~/ros_template_creator/templates/template.launch", "r")
string = data.read()

with open(path, 'a') as f:
  print(string, file=f)
