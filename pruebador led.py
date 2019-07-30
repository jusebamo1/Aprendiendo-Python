#importaciones

import time as t
import RPi.GPIO as GPIO

#Variables de pines
entrada1 = 15
led1=  11
estado = 0

#Setup o configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(entrada1, GPIO.IN)

try:
    
    while 1:
        
        f = GPIO.input(entrada1)
        print(f)
        GPIO.output(led1,GPIO.HIGH)
        t.sleep(0.1)
        GPIO.output(led1,GPIO.LOW)
        t.sleep(0.1)
        
        
except KeyboardInterrupt:
    pass

finally:
    print("Acabé")
    

GPIO.cleanup()
