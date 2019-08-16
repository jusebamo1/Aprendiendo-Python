import time as t
import RPi.GPIO as GPIO

#Variables de pines


led1=  11
led2=  12
led3=  13
led4=  15
led5=  16



#Setup o configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)

#Variable Tamaño leds
ledsList = [led1,led2,led3,led4,led5]


def vumeter(ledsList, entrada):    
    #voy a leer siempre la cantidad de leds disponible
    if entrada == 0:
        GPIO.output(ledsList[0],GPIO.HIGH)
        t.sleep(0.1)
        GPIO.output(ledsList[0],GPIO.LOW)
        t.sleep(0.1)
    else:
        for i in range(entrada):
            
            GPIO.output(ledsList[i],GPIO.HIGH)
            t.sleep(0.1)
            GPIO.output(ledsList[i],GPIO.LOW)
            t.sleep(0.1)
        
def ecuacion(x):
    
    y = (5/6)*x + 15/6
    
    print(y)
    return int(y)





try:
    while 1:
        p = ecuacion(1)
        vumeter(ledsList,p)
        
        
        break
           
        
        
except KeyboardInterrupt:
    
    print("Acabé")
    
finally:
    print("Acabé")
#    for i in range(5):
#            GPIO.output(ledsList[i],GPIO.LOW)
            
            
GPIO.cleanup()