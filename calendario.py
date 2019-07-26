#semana = ("lunes","domingo","sabado","viernes","jueves","miercoles","martes") 
semanaReal = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
semana = []


#busca el dia de la semana...
def BuscarDiadelaSemana(n):
    if (n > 7):
        print(semana[(n%7)-1])    
    else:
        print(semana[n-1]) 

#Orden del dia ingresado...
def OrdenDia(dia):
    print(semanaReal.index(dia))
    x = semanaReal.index(dia)
    y = x-7
    for i in range(x, y , -1):
        #print(semanaReal[i])
        semana.append(semanaReal[i])

        

    


D = OrdenDia(input("Dia de la semana:"))

B = BuscarDiadelaSemana(int(input("# de Dias que quiere retroceder:"))+1)

   
