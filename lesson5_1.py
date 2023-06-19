import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
blue = GPIO.PWM(17, 70)
green = GPIO.PWM(27, 75)
red = GPIO.PWM(22, 75)

i = 75
try:
  while(True):
    red.start(i)  
    sleep(0.5)   
    red.stop()   
    sleep(0.5)

    blue.start(i)  
    sleep(0.5)   
    blue.stop()   
    sleep(0.5) 

    green.start(i)  
    sleep(0.5)   
    green.stop()   
    sleep(0.5)
except KeyboardInterrupt:
    blue.stop() 
    red.stop() 
    green.stop() 
    GPIO.cleanup()
    print("End")
    
