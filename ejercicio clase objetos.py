#importaciones
import time as t

#Ejercicio objetos

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
            t.sleep(2)
            print("....")
            print("Mezclado terminado.")
            break

    def ExpulsarPintura(self,tiempo):

        print("Expulsando Pintura...")
        self.__nivelGas -= 1    
        t.sleep(tiempo)
        print("....")
        print("Expulsion exitosa")
            
        

    def oprimir(self, presionado, tiempo):
        if presionado and self.__nivelGas > 0:
            self.ExpulsarPintura(tiempo)
        elif presionado and self.__nivelGas == 0:
            print("Nivel de gas acabado.")

    def mostarNivel(self):
        return self.__nivelGas



    

PinturaNegra = AerosolPintura("Negro",100,"Blanco")
PinturaNaranja = AerosolPintura("Naranja",50,"Naranja")
PinturaNegra.oprimir(True,2)

print(PinturaNegra.colorDelaPintura)

PinturaNegra.oprimir(True,2)
print(PinturaNegra.mostarNivel())

PinturaNegra.__nivelGas=100
PinturaNegra.oprimir(True,2)
print(PinturaNegra.mostarNivel())

PinturaNegra.Mezclar(5)
print(PinturaNegra.mostarNivel())

######
print(PinturaNaranja.colorDelaPintura)

PinturaNaranja.oprimir(True,2)
print(PinturaNaranja.mostarNivel())

PinturaNaranja.__nivelGas=100
PinturaNaranja.oprimir(True,2)
print(PinturaNaranja.mostarNivel())

PinturaNaranja.Mezclar(5)
print(PinturaNaranja.mostarNivel())