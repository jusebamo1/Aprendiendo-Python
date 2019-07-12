def Menu(): 
    print("1)Agregar nombre \t 2)Agregar Apellido \n3)Eliminar\t4)Ver lista\n5)Salir")

def VerList():
    print("NOMBRES: \t APELLIDOS:")
    print("======================")
    for i in range(len(nombres)):
        print(i,nombres[i], "\t", apellidos[i])

def filtar(cadena):
    #Voy a convertir LAS ENTRADAS A MAYUS
    return cadena.upper()



nombres =[]
apellidos =[]

while True:
    print("Bienvenido")
    Menu()
    opc1 = int(input("Cual desea realizar?:"))
    while opc1 >0 and opc1 <5:
        if opc1 == 1:
            #ADD to list and filter upperCase
            nombres.append(filtar(input("Agregue los Nombres:")))
        elif opc1 == 2:
            #ADD to list and filter upperCase
            apellidos.append(filtar(input("Agregue los Apellidos:")))
        elif opc1 == 3:
            
            #buscar
            f = int(input("posicion de quien quiere eliminar:"))
            #Eliminar
            nombres.pop(f)
            apellidos.pop(f)
            
        elif opc1 == 4:
            VerList()
        else:
            sys.exit()
        break
        
    