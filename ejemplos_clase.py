#!/usr/bin/env python
'''
Listas [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Pedro Lugo"
__email__ = "pllugo@gmail.com"
__version__ = "1.1"

import math

import numpy as np

import matplotlib.pyplot as plt


def practica_listas():
    # 1) Crear una lista que contenga los nùmeros del -10 al 10

    # La lista solicitada es una secuencia numérica ordenada, se puede
    # crear utilizando range

    lista1 = []  # Lista vacia
    range(-10, 10)
    for i in range(-10, 11):
        lista1.append(i)

    # Crear una lista de rango -10 a 10 inclusive

    print('1:', lista1)

    # 2) Crear una lista que contengo unicamente los nùmeros
    # pares entre -10 y 10

    lista2 = []  # Lista vacia
    # Crear una lista de rango -10 a 10 inclusive de 
    # solo nùmeros pares
    for j in range(-10, 11):
        if (j % 2) == 0:
            lista2.append(j)
        else:
            lista2.append(0)

    print('2:', lista2)

    # 3) De la lista1 filtrar los números positivos, es decir,
    # crear una lista a partir de lista1 de solo números positivos

    lista3 = []  # Lista vacia
    # Filtrar numeros positivos
    for y in range(len(lista1)):
        if lista1[y] > 0:
            lista3.append(lista1[y])
        else:
            continue
    print('3:', lista3)

    # 4) De la lista1 filtrar los números mayores a 3, es decir,
    # crear una lista a partir de lista1 de solo números mayores a 3

    lista4 = []  # Lista vacia
    # Filtrar numeros mayores a 3
    for j in range(len(lista1)):
        if lista1[j] > 3:
            lista4.append(lista1[j])
        else:
            continue
    print('4:', lista4)

    # 5) De la lista1 realizar la suma de todos los números

    suma_total = 0
    # Sumar numeros
    for j in range(len(lista1)):
        suma_total = suma_total + lista1[j]

    print('5:', suma_total)

    # 6) De la lista1 realizar el modelo, es decir, pasar todos
    # los números a positivo

    lista6 = []  # Lista vacia
    # Aplicar mdulo
    for i in range(len(lista1)):
        if lista1[i] < 0:
            lista6.append(lista1[i]*-1)
        else:
            lista6.append(lista1[i])

    print('6:', lista6)

    # 7) Calcular la suma entre la lista 1 y la lista 6
    # Como son del mismo utilizar len para calcular el largo
    # y recorrer con indices

    lista7 = []  # Lista vacia
    # Sumar listas
    for i in range(len(lista1)):
        lista7.append(lista1[i] + lista6[i])

    print('7:', lista1)
    print('7:', lista6)
    print('7:', lista7)

    # 8) De la lista1 calcular los números elevados al cuadrado

    lista8 = []  # Lista vacia
    # Elevar al cuadrado
    for i in range(len(lista1)):
        lista8.append(lista1[i] ** 2)
    print('8:', lista8)

    # 9) Crear una lista "x" cuyo rango esté comprendido
    # entre 0 y 4pi, que tenga 40 elementos
    # Calcular la función seno de x
    x = np.linspace(0, 4*math.pi, 40)

    lista9 = []  # Lista vacia
    # # Elevar al cuadrado
    for n in x:
         lista9.append(math.sin(n))


    plt.plot(x, lista9, c='darkblue')
    plt.grid(ls='dashed')
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    practica_listas()
