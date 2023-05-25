import random

minus='abcdefghijklmnñopqrstuvwxyz'
mayus=minus.upper()
numeros='0123456789'
simbolos='@()[]{}+*.,-_¡!?¿<>%$#/=:;'

base = minus+mayus+numeros+simbolos
longitud = 15

for _ in range(5):
    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    print(password)