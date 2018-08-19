import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
while True:
    GPIO.output(18,True)
    GPIO.output(5,False)
    time.sleep(.2)
    GPIO.output(18,False)
    GPIO.output(5,True)
    time.sleep(.2)

    
