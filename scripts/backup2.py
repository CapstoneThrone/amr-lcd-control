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

def get_ip_address():
    return [
             (s.connect(('8.8.8.8', 53)),
              s.getsockname()[0],
              s.close()) for s in
                  [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
           ][0][1]

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("lcdscreen", String, callback)
    # rospy.spin()

if __name__ == '__main__':

    try:

        while 1: 
            lcdbackpack = LcdBackpack('/dev/ttyACM0', 115200)
            lcdbackpack.connect()
            lcdbackpack.clear()
            lcdbackpack.set_backlight_rgb(255,0,255)
            lcdbackpack.set_cursor_home()
        
            lcdbackpack.set_autoscroll(1)
            ip = get_ip_address()
            #lcdbackpack.write(ip)
            lcdbackpack.write("0 1 2 3 4 5 6 7 8 ")
            sleep(1)
            lcdbackpack.clear()
            lcdbackpack.write("1")
            sleep(1)
        
            lcdbackpack.clear()
            #lcdbackpack.write("Voltage: ")
            #lcdbackpack.write("Status:  ")
            #sleep(5)


    #        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
     #       lcd.message('{}'.format(ip))
            
            # Once the backpack has started, waits for listener
            print('Above listener')
            listener()
            print('Below listener')

        
    except KeyboardInterrupt:
        print('CTRL-C pressed.  Program exiting...')


    finally:
        lcdbackpack.clear()

  # Thank you to: https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/

  # Currently using the lcdbackpack library
  # https://github.com/dinofizz/adafruit-usb-serial-lcd-backpack
  # sudo apt install-pip
  # pip install lcdbackpack
  # python lcd.py (Current version is python 2.7)
