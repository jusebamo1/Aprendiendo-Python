#········· Codigo Leds ·············

#importaciones

import time as t
import RPi.GPIO as GPIO

#Variables de pines

entrada1 = 15
led1=  11
led2=  12
led3=  13
led4=  15
led5=  16



#Setup o configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(entrada1, GPIO.IN)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)

#Variable Tamaño leds
SizeLeds = [1,2,3,4,5,6]

try:
    
    while 1:
        
        
        for i in SizeLeds:
            
            if i == 1:
                GPIO.output(led1,GPIO.HIGH)
                t.sleep(0.1)
                GPIO.output(led1,GPIO.LOW)
                t.sleep(0.1)
                
            elif i == 2:
                GPIO.output(led2,GPIO.HIGH)
                t.sleep(0.1)
                GPIO.output(led2,GPIO.LOW)
                t.sleep(0.1)
                
            elif i == 3:
                GPIO.output(led3,GPIO.HIGH)
                t.sleep(0.1)
                GPIO.output(led3,GPIO.LOW)
                t.sleep(0.1)
                
            elif i == 4:
                GPIO.output(led4,GPIO.HIGH)
                t.sleep(0.1)
                GPIO.output(led4,GPIO.LOW)
                t.sleep(0.1)
                
            else:
                GPIO.output(led5,GPIO.HIGH)
                t.sleep(0.1)
                GPIO.output(led5,GPIO.LOW)
                t.sleep(0.1)
        
        
except KeyboardInterrupt:
    pass

finally:
    print("Acabé")
    

GPIO.cleanup()