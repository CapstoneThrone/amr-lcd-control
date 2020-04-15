#!/usr/bin/env python
import rospy
import socket

from std_msgs.msg import String
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
        self.voltage = 0.0
        self.status = ""
        self.error = ""

        self.begin()

    def begin(self):  
        rospy.init_node('subscriber', anonymous=True)
        rospy.Subscriber('lcdscreen1', String, self.string_callback)
        rospy.Subscriber('lcdscreen2', float32, self.float32_callback)
        rospy.spin()          

    def float32_callback(self,msg):
        rospy.loginfo('got string 1 %f', msg.data)
        self.ip = msg.data
        self.backpack()

    def string_callback(self,msg):
        rospy.loginfo('got string 2 %s', msg.data)
        self.status = msg.data
        self.backpack()

    def backpack(self):
        #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
        print("Are we in?") 
        lcdbackpack = LcdBackpack('/dev/ttyACM0', 115200)
        lcdbackpack.connect()
        lcdbackpack.clear()
        lcdbackpack.set_backlight_rgb(255,0,255)
        lcdbackpack.set_cursor_home()
            
    #    lcdbackpack.set_autoscroll(1)
#        ip = get_ip_address()
        
        lcdbackpack.write("IP: " + self.ip)
        lcdbackpack.set_cursor_position(1,2) 
        lcdbackpack.write("V: " + self.voltage)
        sleep(2)
           
        lcdbackpack.clear()   
        lcdbackpack.write("Status: " + self.status)
        lcdbackpack.set_cursor_position(1,2) 
        lcdbackpack.write("Error: " + self.error)
        sleep(2)
           

        lcdbackpack.clear()
                #lcdbackpack.write("Voltage: ")
                #lcdbackpack.write("Status:  ")
                #sleep(5)


        #        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
         #       lcd.message('{}'.format(ip))
                
                # Once the backpack has started, waits for listener
    #            print('Above listener')
     #           listener()
      #          print('Below listener')




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
