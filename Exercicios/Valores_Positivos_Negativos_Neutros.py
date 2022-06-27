#!/usr/bin/env python
# -*- coding:  latin-1 -*-

print(' ---- Tipo de número---- ')
x = int(input("Indique um número: "))
if x < 0:
        print(x,'É um número negativo ')
elif x == 0:
        print(x,'É um número neutro')
elif x > 0:
        print(x,'É um número positivo')
