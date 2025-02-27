from importlib.resources import contents
import random
aleatori = random.randrange(1, 100)    # aleatori contindrà un número enter entre 1 i 9

intents=0 # he inicialitzat el 0 d'intents

for i in range (5):
        intents += 1
        valor = int(input("Quin número he pensat?: ")) # el programa preguna quin número he pensat
        if aleatori > valor: 
            print("El valor pensat és més gran... Torna a provar: ") # no he encertat, el valor pensat és més gran que el que he posat
        elif aleatori < valor:
            print("El valor pensat és més petit... Torna a provar: ") # no he encertat, el valor pensat és més petit que el que he posat
        else:
            print("Molt bé!!! Has endevinat el número secret en " , intents , "intents") # Felicitacions i número d'intents fets
            break