def suma(x, y):
    return x + y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    if y == 0:
        print("No se puede dividir")
    else:   
        return x/y


def potenciacion(x,y):
    return x**y

def divEntera(x,y):
    int(x)
    int(y)
    return x//y

def modulo(x,y):
    return x%y

numeroX = 0


while True:
    if numeroX == 0 or numeroX == None:
        numeroX = float(input("Ingrese numero X:"))
    
    numeroY = float(input("Ingrese numero Y:"))
    print("1) Suma \n2) Resta \n3) Mulplicacion \n4) Divison")
    print("5) Divison Entera  \n6) Potencia \n7) Modulo ")

    opc = int(input("Que funcion realizar:"))
    while opc > 0 and opc < 8 :
        if opc == 1 :
            answer = suma(numeroX,numeroY)
            print(answer)
            break
        elif opc == 2 :
            answer = resta(numeroX,numeroY)
            print(answer)
            break
        elif opc == 3 :
            answer = multiplicacion(numeroX,numeroY)
            print(answer)
            break
        elif opc == 4:
            answer = division(numeroX,numeroY)
            print(answer)
            break
        elif opc == 5 :
            answer = divEntera(numeroX,numeroY)
            print(answer)
            break
        elif opc == 6 :
            answer = potenciacion(numeroX,numeroY)
            print(answer)
            break
        else :
            answer = modulo(numeroX,numeroY)
            print(answer)
            break
    print("Deseas guardar la respuesta?")
    opc2 = str(input(""))
    if opc2 == "si":
        numeroX = answer

    else:
        numeroX = 0        

