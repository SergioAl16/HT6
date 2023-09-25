# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin
19/09/2023

Metdo de Biseccion
"""
from pylab import *
from tabulate import tabulate
from scipy.interpolate import lagrange

def biseccion (a,b,n,d):
    """La funcion implementa el metodo de biseccion para calcular 
    la raiz de la funcion f en el intervalo [a,b] con n interaciones 
    y redondeandoa d decimales"""
    
    x = [0,1,2,3,4,5]
    y = [3.88578E-16,-1.88738E-15,4.88498E-15,-3.55271E-15,1,0]

    f = lagrange(x, y)
    
    xi = float(a); xs = float(b)
    #Convierte el entero a numero de punto flotante o con decimales
    # ; es cambio de linea
    
    x = xi
    fa = f(xi) #Guardar en 'a' mi funcion evaluada en a
    
    x = xs
    fb = f(xs)
    
# Esta es la evalucion de cambio de signo
    if fa*fb > 0:
        return "No se cumple con la condicion de cambio de signo"
   
    elif fa*fb == 0:
        return "Uno de los extremos del intervalo es una raiz"
    
    tabla = [['i','xi','xs','xr','ea'],]
    # --------- TITULO DE LA TABLA 
    # i = iteracion,              ea = error aproximado

    fila = []
    
    ea = float(0)
    
    xr = (xi + xs)/2
    
    for i in range(n):
        
    #Evaluamos el XR
        
        fila = [i,xi,xs,xr,ea]
        redondeados = []
        
#        for i in range(5):
#            redondeados.append(round(fila(i)))

#La funcion de arriba y abajo hacen lo mismo         
   
        for elementos in fila:
            redondeados.append(round(elementos,d))
            
        tabla.append(redondeados) #Mete 'redondeados' a 'fila'
        
        x = xi
        fxi = f(xi)
        
        x = xr
        fxr = f(xr)
        
    #Cuando si hay cambio de signo en el lado de xi para xr ... xs = xr
        if fxi*fxr < 0:
            xs = xr
            
        elif fxi*fxr == 0:
            break 
        #El break termina el ciclo FOR
        
    #Si el cambio de signo esta del otro lado entre xr y xs ... xi = xr
        else:
            xi = xr
            
        xrant = xr
        
        xr = (xi + xs)/2
        
        ea = abs((xr - xrant)/xrant)*100
        
    print (tabulate(tabla))
    print (f(0.85)) # Si se quiere evaluar la funcion en algun punto
    
# HT 6 - PROBLEMA 1
# x = [3,4,3.1,4.5,5.5,6]
# y = [0.141120008, -0.756802495, 0.041580662, -0.977530118, -0.705540326, -0.279415498]

# biseccion (3,4,20,4)

# HT 6 - PROBLEMA 3
# x = [2,3,4,5,6,7]
# y = [-0.000198413,0.005357143,-0.058531746,0.330357143,-1.012698413,1.592857143]
# print (f(0.23))

# biseccion (0,3,20,4)

# HT 6 - PROB 4.1
# x = [0,1,2,3,4,5]
# y = [-0.002036199,0.026244344,-0.106561086,0.066515837,0.515837104,0]
# print(f(0.85))

# biseccion (0,3,20,4)

# HT6 - PROB 4.2
# x = [0,1,2,3,4,5]
# y = [3.88578E-16,-1.88738E-15,4.88498E-15,-3.55271E-15,1,0]
# print(f(0.85))

#  biseccion (0,3,20,4)