#importaciones
import time as t
import RPi.GPIO as GPIO

#Variables de pines
entrada1 = 15
entrada2 = 13
led1= 7
led2= 11
estado = 0

#Setup o configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(entrada1, GPIO.IN)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(entrada2, GPIO.IN)

#sub-Programa

class AerosolPintura():
    #Constructor
    def __init__(self,color,level,colorEnvase):
        self.colorDelaPintura=color
        self.__nivelGas = level
        self.colorEnvase = colorEnvase
        
            

    #Propiedades

    forma = "cilindrica"
    material = "Metalico"
    reciclable = "Si"
    estadoOprimido = False

    #Metodos
    def Mezclar(self,tiempo):

        print("Inicio mezclado...")
        for i in range (tiempo):
            t.sleep(tiempo)
            print("....")
            print("Mezclado terminado.")
            break

    def ExpulsarPintura(self,tiempo, pin):

        print("Expulsando Pintura...")
        self.__nivelGas -= 1
        GPIO.output(pin,GPIO.HIGH)
        t.sleep(tiempo)
        print("....")
        print("Expulsion exitosa")
        GPIO.output(pin,GPIO.LOW)
        

    def oprimir(self, presionado, tiempo,pin):
        if presionado and self.__nivelGas > 0:
            self.ExpulsarPintura(tiempo,pin)
        elif presionado and self.__nivelGas == 0:
            print("Nivel de gas acabado.")

    def mostrarNivel(self):
        return self.__nivelGas



Pinturaverde = AerosolPintura("Verde",100,"Verde")
PinturaRoja =  AerosolPintura("Roja",50,"Roja")



try:
    while 1:
        
        f = GPIO.input(entrada1)
        Pinturaverde.oprimir(f,0.5,led1)
        #print(Pinturaverde.mostrarNivel())
        g = GPIO.input(entrada2)
        PinturaRoja.oprimir(g,0.5,led2)
        
        
        
    
    
except KeyboardInterrupt:
    pass

finally:
    print("Acabé")
    

GPIO.cleanup()