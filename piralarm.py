# detects motion sensor from PIR Sensor Module attached to GPIO 17.
# change [MediaFile] in path to name of media file in Music folder.

import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

while True:
    if GPIO.input(17):
        os.system("omxplayer -o hdmi /home/pi/Music/[Media File].m4v")