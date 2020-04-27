import numpy as np

f = np.array([[3,4,"tipo3"],[1,2,"grupo4"],[5,6,"clase2"],[5,6,"clase3"]])

def organizador(f):
    for i in range(len(f)):
        for j in range(len(f)):
            if f[i,2] < [j,2]:
                for k in range(len(f[0])):
                    K = f[j,k]
                    f[j,h] = f[i,f]
                    f[i,k]= K

