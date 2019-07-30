#importaciones

import time as t
import RPi.GPIO as GPIO

#Variables de pines
entrada1 = 11
led1= 7
estado = 0

#Setup o configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(entrada1, GPIO.IN)


#subprograma:
def filtro(lectura, estado):
    
    
    if lectura == 1 and estado==1:
            estado = 0
            t.sleep(0.2)
            return estado
        
    elif lectura == 1 and estado==0:
            estado = 1
            t.sleep(0.2)
            return estado
            

#Programa Principal
try:
    
    while 1:
        
        f= filtro(GPIO.input(entrada1),estado)
        print(estado)
        
        if f == 1:
            GPIO.output(led1,GPIO.HIGH)
            t.sleep(0.5)
        elif f == 0:
            GPIO.output(led1,GPIO.LOW)
            t.sleep(0.5)
          
            
        
        
        
        
        '''
        GPIO.output(led1,GPIO.HIGH)
        t.sleep(0.1)
        GPIO.output(led1,GPIO.LOW)
        t.sleep(0.1)
        '''
except KeyboardInterrupt:
    pass

finally:
    print("Acabé")
    

GPIO.cleanup()

