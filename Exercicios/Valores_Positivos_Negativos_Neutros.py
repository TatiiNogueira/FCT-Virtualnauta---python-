#!/usr/bin/env python
# -*- coding:  latin-1 -*-

print(' ---- Tipo de n�mero---- ')
x = int(input("Indique um n�mero: "))
if x < 0:
        print(x,'� um n�mero negativo ')
elif x == 0:
        print(x,'� um n�mero neutro')
elif x > 0:
        print(x,'� um n�mero positivo')
