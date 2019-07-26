#semana = ("lunes","domingo","sabado","viernes","jueves","miercoles","martes") 
semanaReal = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
Meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
mes = []
semana = []

<<<<<<< HEAD

=======
cuentaM = 0
n = 0
>>>>>>> dec39aa33baa5a616adb2104d0bdabe983317a54
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
<<<<<<< HEAD
        semana.append(semanaReal[i])
=======
        semana.append(semanaReal[i])    
>>>>>>> dec39aa33baa5a616adb2104d0bdabe983317a54

def OrdenMes(cadenaMes, cadenaMes2):
    print(Meses.index(cadenaMes))
    x = Meses.index(cadenaMes)
    y = Meses.index(cadenaMes2)
    for i in range(x, y , -1):
        #print(Meses[i-1])
        mes.append(Meses[i-1])

def conocerMes(cadenaMes):
    m = Meses.index(cadenaMes)
    m += 1
    if m == 2 :
        #print("Su mes tiene 28 dias")
        return 28
    elif m % 2 == 0  and m  <= 7:
        #print("Su mes tiene 30 dias")
        return 30
    elif m % 2 != 0 and m <= 7:
        #print ("Su mes tiene 31 dias")
        return 31
    elif m%2 == 0 and m > 7:
        #print("Su mes tiene 31 dias")
        return 31
    elif m%2 != 0 and m > 7 :
        #print("Su mes tiene 30 dias")
        return 30
        



<<<<<<< HEAD

D = OrdenDia(input("Dia de la semana:"))

B = BuscarDiadelaSemana(int(input("# de Dias que quiere retroceder:"))+1)

   
=======
while True :
    dow = (input("Dia de la semana actual:"))
    # numero del dia de hoy
    numberDate = int(input("Numero del dia actual:"))
    #B = BuscarDiadelaSemana(int(input("# de Dias que quiere retroceder:"))+1)
    mounth = (input("Mes actual:"))
    #year = (int(input("Año actual:")))
    #M = conocerMes(input("Mes actual:"))

    date2 = int(input("Numero del dia a buscar:")) 
    mounth2= (input("Mes a buscar:"))
    #year2 = (int(input("Año a buscar:")))
    (OrdenMes(mounth, mounth2 ))

    cuenta = numberDate +1
    for i in mes:
        print(i)
        cuenta += conocerMes(i)

    cuenta -= date2
    OrdenDia(dow)
    BuscarDiadelaSemana(cuenta)
    cuenta=0

    
>>>>>>> dec39aa33baa5a616adb2104d0bdabe983317a54
