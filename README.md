# amr-lcd-control

This repo is used to control a 2 by 16 LCD screen that prints out informaiton about the current
operation of the raspberyr pi. Currently, the LCD screen prints information with the given 
data types:

- IP address (String)
- Voltage    (float32)
- Status     (String)
- Errors     (String)

This repository should be cloned into the /path/to/catkin_ws/src/ directory. Following the cloning, the package
needs to be built

$ cd ~/catkin_ws
$ catkin_make

The repo uses a subscriber node to collect information from the publisher nodes. All nodes can 
be started with the roslaunch command. Also, roslaunch will automatically start roscore if it 
detects that it is not already running

$ roslaunch amr-lcd-control main.launch

To view our publisher and subscriber nodes, head into /path/to/amr-lcd-contorl/scripts. To view the topics our nodes are publishing to and subscribing to, use the command:

$ rostopic list
$ rostopic -h      // Use for the help menu



