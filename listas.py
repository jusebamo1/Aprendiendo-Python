def Menu(): 
    import os,sys
    print("Bienvenido")
    print("")
    print("1)Agregar nombre\n2)Agregar Apellido\n3)Eliminar\n4)Ver lista\n5)Salir")

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
    print("")
    Menu()
    try:
        opc1 = int(input("Introduzca el número de la opcion a realizar:"))
    except:
        print("--- Eso no es un número, por favor introduce un número...")  

        Menu()
    opc1 = opc1
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
        
    
