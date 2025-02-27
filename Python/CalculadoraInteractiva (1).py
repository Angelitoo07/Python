numero1=int(input("Insereix un numero: ")) # Per inserir el primer número
numero2=int(input("Insereix un altre numero: ")) # Per inserir el segon número

elecció=0 

while elecció != 6: # Número per escollir el simbol de l'operació
    print("""
    Indica l'operacio que vols fer:
    
    1) +
    2) -
    3) *
    4) /
    5) %
    """)

    elecció=int(input())

    if elecció == 1: # Si diem que volem el número 1
        print(" ")
        print("Resultat: ", numero1,"+", numero2,"=",numero1+numero2) # Sumarà el primer número amb el segon

    elif elecció == 2:
        print(" ")
        print("Resultat:", numero1, "-", numero2, "=",numero1-numero2) # Restarà el primer número amb el segon

    elif elecció == 3:
        print(" ")
        print("Resultat:", numero1, "*", numero2, "=",numero1*numero2) # Multiplicarà el primer número amb el segon

    elif elecció == 4:
        print(" ")
        print("Resultat:", numero1, "/", numero2, "=",numero1/numero2) # Dividirà el primer número amb el segon

    elif elecció == 5:
        print(" ")
        print("Resultat:", numero1, "%", numero2, "=",numero1%numero2) # Donarà el residu de la divisió feta entre el primer número amb el segon
    
    