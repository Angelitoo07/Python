import random 
aleatori = random.randrange(1, 9)    # aleatori contindrà un número enter entre 1 i 9
print("Aquest es el primer número: " , aleatori)

aleatori2 = random.randrange(1, 9)    # aleatori contindrà un número enter entre 1 i 9
print("Aquest es el segon número: " , aleatori2)

simbol1="l+-*/" #simbol aleatori
simbol = random.randrange(1, 5)    # número aleatori
print("Aquest es el segon número: " , simbol1[simbol])

resultat=input("Insereix la teva resposta: " ) # depenent del número aletori anterior, aquest contindrà un simbol
print (round(float(resultat))) #Aquets son els simbols que poden sortir aleatoriament
if simbol == 1: # si surt 1...
    resultatord = aleatori + aleatori2 # sumar primer número aleatori amb el segon

elif simbol == 2: # si surt 2...
    resultatord = aleatori - aleatori2 # restar primer número aleatori amb el segon

elif simbol == 3: # msi surt 3...
    resultatord = aleatori * aleatori2 # multiplicar primer número aleatori amb el segon

elif simbol == 4: # si surt 4...
    resultatord = aleatori / aleatori2 # dividir primer número aleatori amb el segon


if int(resultat) == int(resultatord): 
    print("Correcte") # Si la resposta es correcte sortirà la paraula "Correcte"
else:
    print("Incorrecte") # Si la resposta es incorrecte sortirà la paraula "Incorrecte"