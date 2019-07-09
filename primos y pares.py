def notIsPrimo(x):
    for i in range( x-1, 1, -1):


        #print(i , " ",x % i)
        
        if x % i ==  0 :
            #print("no es primo")
            
            return 1
    
    return 0


numero = int(input ("Ingrese el numero:"))
#print (notIsPrimo(numero))
if notIsPrimo(numero):
    print("no es primo")

else:
    print("el numero es primo")

            



     




