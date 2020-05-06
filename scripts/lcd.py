#!/usr/bin/env python
import rospy
import socket

from std_msgs.msg import String
from std_msgs.msg import Float32
from time import sleep, strftime
from datetime import datetime
from lcdbackpack import LcdBackpack

class MySubscriber(object):
    def __init__(self):

#new ip code
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)	
#
        self.ip = IPAddr
        self.voltage = ""
        self.status = ""
        self.error = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"

        self.begin()

    def begin(self):  
        rospy.init_node('subscriber', anonymous=True)
        rospy.Subscriber('lcdscreen1', String, self.string_callback)
        rospy.Subscriber('mcVoltage', Float32, self.float32_callback)
        rospy.spin()          

    def float32_callback(self,msg):
        rospy.logdebug(msg.data)
        self.voltage = str(msg.data)
        self.backpack()

    def string_callback(self,msg):
        rospy.logdebug('got string 2 %s', msg.data)
        self.status = msg.data
        self.backpack()

    def backpack(self):
        #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
        #print("Are we in?") 
        lcdbackpack = LcdBackpack('/dev/ttyACM0', 115200)
        lcdbackpack.connect()
        lcdbackpack.clear()
        lcdbackpack.set_backlight_rgb(255,0,255)
        lcdbackpack.set_cursor_home()
            
    #    lcdbackpack.set_autoscroll(1)
       
        
        lcdbackpack.write("IP: " + self.ip)
    #    lcdbackpack.set_cursor_position(1,2) 
        sleep(3)
        lcdbackpack.clear()
        
        lcdbackpack.write("V: " + self.voltage)
        sleep(3)
        lcdbackpack.clear()   

        lcdbackpack.write("Status: " + self.status)
        sleep(3)
        lcdbackpack.clear()

       # lcdbackpack.set_cursor_position(1,2) 
        lcdbackpack.write("Error: " + self.error)
        sleep(3)
        lcdbackpack.clear()
        #        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
         #       lcd.message('{}'.format(ip))

if __name__ == '__main__':
    try:
        MySubscriber()
    except KeyboardInterrupt:
        print('CTRL-C pressed. Program exiting...')









  # Currently using the lcdbackpack library
  # https://github.com/dinofizz/adafruit-usb-serial-lcd-backpack
  # sudo apt install-pip
  # pip install lcdbackpack
  # python lcd.py (Current version is python 2.7)
