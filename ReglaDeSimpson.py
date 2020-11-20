import numpy as np

def f(x):
    return x**3 - x + 1

def usarSimpson(y : np.array, inicio : float, fin : float, deltaX : float):
    count = 0 # hacemos un contador
    for i in range(len(y)): # por cada uno de los puntos vamos a checar lo que seigue
        if i == 0 or i == len(y) - 1: # si es el inicio o el fin agregamos el punto a nuestra cuenta
            count += y[i]
        elif i % 2 == 1: # si es un numero impar, multiplicamos y * 4 para decir que es el punto medio
            count += y[i] * 4
        elif i % 2 == 0: # si es un numero par, multiplicamos y * 2 para decir que es el de lado, pero como tiene 2 partes es * 2
            count += y[i] * 2
    return (deltaX / 3) * count

def correr():
    # constantes
    xInicial = -1
    xFinal = 1

    n = 10 * 2 # hacemos por 2, para hacer separacion por cortes, y luego sacamos el final

    h = (xFinal - xInicial) / n # conocido tambien como deltaX

    x = np.arange(xInicial, xFinal + h, h) # hacemos el +h para que termine en el ultimo

    y = f(x) # hacemos que y sean los valores de la formula

    print(usarSimpson(y,xInicial,xFinal,h)) # imprimimos la formula usada

correr()