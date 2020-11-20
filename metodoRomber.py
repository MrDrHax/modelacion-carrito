import numpy as np

def f(x):
    return np.sin(x)

def trapecio(x_low, x_up, quantity):
    dx = (x_up - x_low)/quantity
    x = np.linspace(x_low, x_up - dx, quantity)
    x_list = (x[0],x[-1])
    x_ends = np.array(x_list)
    np.delete(x,0)
    np.delete(x,-1)
    mid = np.sum(dx*f(x))
    ends = np.sum((dx/2)*f(x_ends))
    return mid + ends

def formulizca(n, startPoint, endPoint):
    matriz = np.zeros((n,n))

    for i in range(n):
        # aqui ponemos la cosa para llenar la primer fila
        # seleccionamos nuestra celda
        matriz[i ,0] = trapecio(startPoint, endPoint, 2 ** i)
    
    for j in range(1, n):
        for i in range(j, n):
            # llenamos las cosas
            matriz[i,j] = (4 ** (j) * matriz[i,j-1] - matriz[i - 1,j - 1])/ (4**(j)-1)

    print(matriz)

formulizca(10, 0, np.pi)
