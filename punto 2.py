#se rompe si es menor o mayor a 3x3

matriz = []

filas = int(input("ingrese numero de filas: "))
columnas = int(input("ingrese munero de columnas: "))

for i in range(filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input((f,c)))

print(matriz)


def funcion_acendente(lista):
    for a in range(len(lista)-1,0,-1):
        for b in range(a):
            if lista[b] > lista[b + 1]:
                temp = lista[b]
                lista[b] = lista[b + 1]
                lista[b + 1] = temp



def funcion_decendente(lista):
    for a in range(len(lista)-1,0,-1):
        for b in range(a):
            if lista[b] < lista[b + 1]:
                temp = lista[b]
                lista[b] = lista[b + 1]
                lista[b + 1] = temp
    

for filas in range(0,filas,1):
    vector1 = matriz[0]
    vector2 = matriz[1]
    vector3 = matriz[2]
    


print(" ")
def Funcionando():
        
    funcion_acendente(vector1)
    print(vector1)

    funcion_decendente(vector2)
    print(vector2)

    funcion_acendente(vector3)
    print(vector3)

Funcionando()