# Regla del trapecio

import numpy as np

def f(x):
    return x**2

def trapecio(x_low, x_up):
    dx = (x_up - x_low)/500
    x = np.linspace(x_low, x_up - dx, 500)
    x_list = (x[0],x[-1])
    x_ends = np.array(x_list)
    np.delete(x,0)
    np.delete(x,-1)
    mid = np.sum(dx*f(x))
    ends = np.sum((dx/2)*f(x_ends))
    return mid + ends

def main():
    x_low = float(input("Ingrese el valor mínimo\n"))
    x_up = float(input("Ingrese el valor máximo\n"))
    print("La aproximación es",trapecio(x_low, x_up))
    return 0

main()
