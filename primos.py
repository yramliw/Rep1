#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Números primos

def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #de lo contrario devuelve Verdadero

print es_primo(8)

import time
print (time.strftime("%H:%M:%S"))
print (time.strftime("%d/%m/%y"))
