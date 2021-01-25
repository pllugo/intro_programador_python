#!/usr/bin/env python
'''
Listas [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Lugo"
__email__ = "pllugo@gmail.com"
__version__ = "1.2"

import math


def practica_listas():
    # 1) Crear una lista que contenga los nùmeros del -5 al 5

    # La lista solicitada es una secuencia numérica ordenada, se puede
    # crear utilizando range

    lista1 = []  # Lista vacia

    # Crear una lista de rango -5 a 5 inclusive
    for i in range(-5,6):
        lista1.append(i)

    print('1:', lista1)

    # 2) Crear una lista que contengo unicamente los nùmeros
    # impares entre -5 y 5

    lista2 = []  # Lista vacia
    # Crear una lista de rango -5 a 5 inclusive de 
    # solo nùmeros impares
    for i in range(len(lista1)):
        if (lista1[i] % 2 != 0):
            lista2.append(lista1[i])
        else:
            continue
    print('2:', lista2)

    # 3) De la lista1 filtrar los números negativos, es decir,
    # crear una lista a partir de lista1 de solo números negativos

    lista3 = []  # Lista vacia
    # Filtrar numeros negativos
    for i in range(len(lista1)):
        if lista1[i] < 0:
            lista3.append(lista1[i])
        else:
            continue
    print('3:', lista3)

    # 4) De la lista1 filtrar los números mayores a 2, es decir,
    # crear una lista a partir de lista1 de solo números mayores a 2

    lista4 = []  # Lista vacia
    # Filtrar numeros mayores a 2
    for n in lista1:
        if n > 2:
            lista4.append(n)

    print('4:', lista4)

    # 5) De la lista1 realizar la suma de todos los números

    suma_total = 0
    # Sumar numeros
    for i in lista1:
        suma_total = suma_total + lista1[i]
    print('5:', suma_total)

    # 6) De la lista1 realizar el modelo, es decir, pasar todos
    # los números a positivo

    lista6 = []  # Lista vacia
    # Aplicar mdulo
    for i in lista1:
        if lista1[i] < 0:
            lista6.append(lista1[i] * -1)
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

    # 8) De la lista1 calcular multiplicar por dos todos los números

    lista8 = []  # Lista vacia
    # Multiplicar por dos
    for i in range(len(lista1)):
        lista8.append(lista1[i] * 2)
    print('8:', lista8)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    practica_listas()
