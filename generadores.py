#Generadores

def multiplos2 (limite):
    num = 1
    while num <= limite:
        num *= 2
        yield num
        
        
pares = multiplos2(10000000)
print(type(pares))

for i in range(1, 6):

    if i == 5:
        print(next(pares))
        break
        
    next(pares)
    
    
'''    
print("primer multiplo: ", next(pares))
print("segundo multiplo: ", next(pares))

print("******************************")

print("tercer multiplo: ", next(pares))
print("cuarto multiplo: ", next(pares))
'''