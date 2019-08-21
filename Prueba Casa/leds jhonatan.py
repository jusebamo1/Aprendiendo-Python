
import random as r

listadoPines = [10, 11, 12, 13, 14, 15]


def funcion_toogle(estado, pin):
    if estado == 1:
        print(1, pin)
    else:
        print(0, pin)



limite = 6 #este es el tamaño del Array
inicio = (limite//2) #Lo divido en 2 para que el sistema sepa cual es el punto 0 del eje x

##Ingreso el valor de volumen
ledsPrendidos = int(input("Digite el numero que desea:"))



if( ledsPrendidos > 0):

    
    ##Enciende desde inicio hasta el limite
    for i in range(inicio, limite, 1):
        funcion_toogle(1, listadoPines[i])


    print("---------")

    for i in range(inicio+ledsPrendidos, limite, 1):
        funcion_toogle(0, listadoPines[i])


elif(ledsPrendidos < 0):

    ledsPrendidos = abs(ledsPrendidos)
    ##Enciende desde inicio hasta el limite hacia abajo RECIBE SOLO VALORES ABSOLUTOS
    for i in range(inicio-1, -1, -1):
        funcion_toogle(1, listadoPines[i])

    
    print("---------")
    #Apaga desde el inicio hasta el limite de leds prendidos
    for i in range(0, inicio - ledsPrendidos, 1):
        funcion_toogle(0, listadoPines[i])

elif(ledsPrendidos==0):
    for i in range(0, limite , 1):
        funcion_toogle(0, listadoPines[i])