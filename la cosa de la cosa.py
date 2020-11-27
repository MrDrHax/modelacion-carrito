from numpy.core.defchararray import array
import streamlit as str
import numpy as np
import matplotlib.pyplot as plt

# parte 1, funcion de la curba 

def sacarFormula(coordenadasX : list, coordenadasY : list): # sacar los valores de a, b, c , d, considerando coordenadas
    p = np.polyfit(coordenadasX, coordenadasY,3)

    f = np.poly1d(p)

    print(p,f)

    return f

def sacarRadio(punto1, punto2, punto3):
    puntosMedios1 = ( (punto1[0] + punto2[0]) / 2 , (punto1[1] + punto2[1]) / 2 ) # punto medio entre los 3 puntos
    puntosMedios2 = ( (punto3[0] + punto2[0]) / 2 , (punto3[1] + punto2[1]) / 2 )

    slope1 = (punto2[1] - punto1[1])/(punto2[0] - punto1[0]) # slope of each thing
    slope2 = (punto3[1] - punto2[1])/(punto3[0] - punto2[0])

    perpendicularSlope1 = -((slope1) ** (-1)) # slope of the prependicular line
    perpendicularSlope2 = -(1/slope2) 

    # aqui vemos por donde pasa la cosa, y ya tenemos b y a para hacer la interseccion
    b1 = puntosMedios1[1] - perpendicularSlope1 * puntosMedios1[0] # b = y - ax
    b2 = puntosMedios2[1] - perpendicularSlope2 * puntosMedios2[0] 

    # consideramos la siguiente formula para sacar x
    # x (a1 - a2) = b2-b1
    # a siendo el slope, b siendo el suma

    x = (b2-b1) / (perpendicularSlope1 - perpendicularSlope2)
    y = perpendicularSlope1 * x + b1

    # sacamos la distancia entre un punto inicial al actual 

    distancia = np.sqrt((x - punto1[0]) ** 2 + (y - punto1[1]) ** 2)

    return distancia, x, y


def sacarTangente(idPunto, x, y):
    return (y[idPunto - 1] - y[idPunto + 1])/(x[idPunto - 1] - x[idPunto + 1])

def tangente(slope, vel, puntoInicial): 
    grados = np.arctan(slope)
    x = (puntoInicial[0], puntoInicial[0] - np.cos(grados) * vel)
    y = (puntoInicial[1], puntoInicial[1] - np.sin(grados) * vel)
    return x,y

# parte 2, graficando

def hacerPlot(f, rangoX, tangente_x,tangente_y, punto1, punto2, punto3, punto4):
    if not str.checkbox("escalar bien"):

        plt.plot(rangoX, f(rangoX)) 
        plt.plot(tangente_x, tangente_y)
        plt.scatter(punto1[0], punto1[1])
        plt.scatter(punto2[0], punto2[1])
        plt.scatter(punto3[0], punto3[1])
        plt.scatter(punto4[0], punto4[1])

        plt.xlim([500,4400])
        plt.ylim([-900,3000])

        # cambia esto para enfocar todo (no escalado)
        # plt.xlim([800,2900])
        # plt.ylim([-9000,3000])

        str.pyplot(plt)
    
    else:
        plt.plot(rangoX, f(rangoX)) 
        plt.plot(tangente_x, tangente_y)
        plt.scatter(punto1[0], punto1[1])
        plt.scatter(punto2[0], punto2[1])
        plt.scatter(punto3[0], punto3[1])
        plt.scatter(punto4[0], punto4[1])

        plt.xlim([punto3[0] - 500, punto3[0] + 500])
        plt.ylim([punto3[1] - 500, punto3[1] + 500])

        str.pyplot(plt)

def sacarAnguloEnRad(slope):
    grados = np.arctan(slope)
    return grados

def sacarDiferenciaEntre2Slopes(slope1, slope2):
    grados1 = sacarAnguloEnRad(slope1)
    grados2 = sacarAnguloEnRad(slope2)

    rad = grados1 - grados2

    deg = np.degrees(rad)

    return deg

# parte 3, interfaz grafica

str.markdown('wewooo')

xInicial = str.slider("X inicial",0,3000,0,100)
xFinal = str.slider("X final",0,3000,0,100)
Puntos = str.slider ("cantidad de puntos", 50,500)

# pedir numero de variables x, y

cantidadDeVariables = str.number_input("cantidad de coordenadas:", value=1)
listaX = []
listaY = []

arregloX, arregloY = str.beta_columns(2)

with arregloX:
    str.text("X")
    for i in range(cantidadDeVariables):
        listaX.append(str.slider("",0,3000,0,100,key = f"x{i}")) # otro slider aqui

with arregloY:
    str.text("Y")
    for i in range(cantidadDeVariables):
        listaY.append(str.slider("",0,3000,0,100,key = f"y{i}")) # otro slider aqui

puntoTangente = str.slider("enfocar el punto:",1 , Puntos - 1)

punto2Circulo = puntoTangente - 2

f = sacarFormula(listaX, listaY)

arrayDeX = np.linspace(xInicial,xFinal, Puntos)

radio, x, y = sacarRadio((arrayDeX[puntoTangente], f(arrayDeX[puntoTangente])) , (arrayDeX[int((puntoTangente + punto2Circulo) / 2)], f(arrayDeX[int((puntoTangente + punto2Circulo) / 2)])) , (arrayDeX[punto2Circulo], f(arrayDeX[punto2Circulo])))

str.text(f"Radio = {radio}, X = {x}, Y = {y}.") # UwU

a = sacarTangente(puntoTangente, arrayDeX, f(arrayDeX))

benches = ((1320, 1400, 1380, 1300, 1320 ),(-650, -720, -740, -670,-650))

plt.plot(benches[0], benches[1])

lineaTangenteX, lineaTangenteY = tangente(a, radio * 0.8 , (arrayDeX[puntoTangente], f(arrayDeX[puntoTangente])))
str.markdown(f"valor de la tangente: {a:.2f}, en el punto {arrayDeX[puntoTangente]}")

hacerPlot(f, arrayDeX, lineaTangenteX, lineaTangenteY,(x,y), (arrayDeX[punto2Circulo], f(arrayDeX[punto2Circulo])), (arrayDeX[int((puntoTangente + punto2Circulo) / 2)], f(arrayDeX[int((puntoTangente + punto2Circulo) / 2)])), (arrayDeX[puntoTangente], f(arrayDeX[puntoTangente])))

str.text(f"Los valores importantes que podemos tener incluyen:\nX min = {xInicial}\nX max = {xFinal}\npos seleccionada: {arrayDeX[puntoTangente]}, {f(arrayDeX[puntoTangente])}")
str.text(f"formula es: {f}")

diferencia = sacarDiferenciaEntre2Slopes(sacarTangente(puntoTangente, arrayDeX, f(arrayDeX)), sacarTangente(puntoTangente - 1, arrayDeX, f(arrayDeX)))

str.text(f"angulo de diferencia = {diferencia}")