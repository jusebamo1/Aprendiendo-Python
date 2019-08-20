#·······replica leds··········
import time as t
import RPi.GPIO as GPIO
import random

#Variables de pines
led1=  11
led2=  12
led3=  13
led4=  15
led5=  16
led6=  18

#Setup o configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)

#Variable Tamaño leds
ledsList = [led1,led2,led3,led4,led5,led6]

#Definiciones
limite = 6 #este es el tamaño del Array
inicio = (limite//2) #Lo divido en 2 para que el sistema sepa cual es el punto 0 del eje x


def nivel(ledsPrendidos):
    
   
    if( ledsPrendidos > 0):

        ##Enciende desde inicio hasta el limite
        for i in range(inicio, limite, 1):
            #funcion_toogle(1, listadoPines[i])
            GPIO.output(ledsList[i],GPIO.HIGH)
            
        for i in range(inicio+ledsPrendidos, limite, 1):
            GPIO.output(ledsList[i],GPIO.LOW)

        
    elif(ledsPrendidos < 0):

        ledsPrendidos = abs(ledsPrendidos)
        ##Enciende desde inicio hasta el limite hacia abajo RECIBE SOLO VALORES ABSOLUTOS
        for i in range(inicio-1, -1, -1):
            GPIO.output(ledsList[i],GPIO.HIGH)

        #Apaga desde el inicio hasta el limite de leds prendidos
        for i in range(0, inicio - ledsPrendidos, 1):
            GPIO.output(ledsList[i],GPIO.LOW)

    elif(ledsPrendidos==0):
        for i in range(0, limite , 1):
            GPIO.output(ledsList[i],GPIO.LOW)






    
