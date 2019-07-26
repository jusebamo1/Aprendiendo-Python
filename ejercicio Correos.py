correo = "4#duro@gmail.com"

def correos():
    correo = input("Introduzca su correo:")

def detector():
    for i in correo:
        yield i

    
detect = detector()

for i in detect:
    
    if(i >="0" and i <= "9" or i>= "A" and i<= "Z" or i>= "a" and i<= "z" or i =="@"):
        print("es valido")
    else:
        print("no es valido")
    