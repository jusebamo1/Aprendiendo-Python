def Menu(): 
    print("1)Agregar nombre \t 2)Agregar Apellido \n3)Eliminar\t4)Ver lista")

def VerList():
    print("NOMBRES: \t APELLIDOS:")
    print("======================")
    for i in range(len(nombres)):
        print(nombres[i], "\t", apellidos[i] )

    

nombres =[]
apellidos =[]

while True:
    print("Bienvenido")
    Menu()
    opc1 = int(input("Cual desea realizar?:"))
    while opc1 >0 and opc1 <5:
        if opc1 == 1:
            nombres.append(input("Agregue los Nombres:"))
        elif opc1 == 2:
            apellidos.append(input("Agregue los Apellidos:"))
        elif opc1 == 3:
            nombres.remove(input("Nombre que quiere eliminar:"))
        elif opc1 == 4:
            VerList()
        break
        
    