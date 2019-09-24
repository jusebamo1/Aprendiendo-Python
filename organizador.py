n = [103,108,100,1245,2,1]


for i in range(len(n)-1):
    x=n[i]
    y=n[i+1]
    
    if x > y :
        memory= x
        n[i] = y
        n[i+1]= memory

    for i in range(len(n)-1):
        x=n[i]
        y=n[i+1]
        
        if x > y :
            memory= x
            n[i] = y
            n[i+1]= memory


        
print(n)
        


    


    