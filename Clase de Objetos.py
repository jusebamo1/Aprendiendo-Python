import time as T

#Clase objetos

class 	Carro():
	#Propiedades

	color = "Gris"
	marca = "Ford"
	cilidrajeDeCarro = 2.0



	#Metodos || Acciones
	def encender(self, tiempo, nombreDuenio):
		
		print("Encendiendo")
		for i in range(tiempo):
			T.sleep(1)
			print("....")

		print("Encendido carro" + nombreDuenio )





#instanciar un objeto
MiCarro = Carro()
CarroProfesor = Carro()

#Cambbiar la propiedad de un objeto
CarroProfesor.color = "Rojo"


print(MiCarro.color) 

print(CarroProfesor.color) 
CarroProfesor.encender(2, "Jonathan")
MiCarro.encender(1, "Sebastian")