#!/usr/bin/env python
import rospy
import socket

from std_msgs.msg import String
from time import sleep, strftime
from datetime import datetime
from lcdbackpack import LcdBackpack


#  Initialize LCD (must specify pinout and dimensions)
#lcd = Adafruit_CharLCD(rs=26, en=19,
#                       d4=13, d5=6, d6=5, d7=11,
#                       cols=16, lines=2)

class MySubscriber(object):
    def __init__(self):
        self.ip = ""
        self.voltage = ""
        self.status = ""
        self.error = ""
        
        
        rospy.init_node('subscriber', anonymous=True)
        rospy.Subscriber('lcdscreen1', String, self.string1_callback)
        rospy.Subscriber('lcdscreen2', String, self.string2_callback)
        rospy.spin()
   #     self.contr_obj = ControlValuePub(kp=1, kd=0.1, dt=10)

    def string1_callback(self,msg):
        rospy.loginfo('got string 1 %s', msg.data)
        self.voltage = msg.data

    def string2_callback(self,msg):
    # This callback is the boss, it dictates the publish rate
        rospy.loginfo('got string 2 %s', msg.data)
        self.status = msg.data


if __name__ == '__main__':
    try:
        MySubscriber()
    except KeyboardInterrupt:
        print('CTRL-C pressed. Program exiting...')


















def get_ip_address():
    return [
             (s.connect(('8.8.8.8', 53)),
              s.getsockname()[0],
              s.close()) for s in
                  [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
           ][0][1]

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    
    lcdbackpack = LcdBackpack('/dev/ttyACM0', 115200)
    lcdbackpack.connect()
    lcdbackpack.clear()
    lcdbackpack.set_backlight_rgb(255,0,255)
    lcdbackpack.set_cursor_home()
        
#    lcdbackpack.set_autoscroll(1)
    ip = get_ip_address()
    lcdbackpack.write(ip)
    lcdbackpack.write("Voltage: " + data.data)
#    lcdbackpack.write("0 1 2 3 4 5 6 7 8 ")
    sleep(1)
 #   lcdbackpack.clear()
 #   lcdbackpack.write("1")
 #   sleep(1)
        
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


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("lcdscreen", String, callback)
    rospy.spin()

# if __name__ == '__main__':

#    try:

#        listener() 
        
#    except KeyboardInterrupt:
#        print('CTRL-C pressed.  Program exiting...')


#    finally:
#        lcdbackpack.clear()

  # Thank you to: https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/

  # Currently using the lcdbackpack library
  # https://github.com/dinofizz/adafruit-usb-serial-lcd-backpack
  # sudo apt install-pip
  # pip install lcdbackpack
  # python lcd.py (Current version is python 2.7)
