import time as t

#Ejercicio objetos

class AerosolPintura():
	#Propiedades

	forma = "cilindrica"
	colorDelaPintura= "Amarillo"
	colorEnvase = "Amarillo y negro"
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

	def ExpulsarPintura(self, nivelGas):

		print("Expulsando Pintura...")
		
		for i in range (nivelGas):	
			t.sleep(1)
			print("....")
			print("Expulsion exitosa")
			
		

	def oprimir(self, presionado):
		if presionado:
			self.ExpulsarPintura (self.100)
			#pass


	

PinturaNegra = AerosolPintura()
PinturaNegra.oprimir(True);




