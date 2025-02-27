# Inicialitzem una llista per emmagatzemar els plats y preus
plat = [] 
preu = []
preutotal = 0


numero_de_plats = int(input("¿Quants plats desitges afegir al menú? ")) # Definim el número de plats que es desitgen ingresar

for i in range(numero_de_plats): # Ustilitzem un bucle for per solicitar els plats y preus

    plat.append(input(f"Insereix el nom del plat: "))     # Demanem el nom del plat
    
    preu.append(int(input(f"Insereix el preu del plat: ")))     # Demanem el preu del plat

print("\nMenú del restaurant: \n----------------") # Imprimim el menú final
for i in range(numero_de_plats):
    print(f"{i+1}. {plat[i]}:  {preu[i]}€")
print("----------------")

while True:
    comanda_per_dinar=int(input("Que voleu dinar? ")) # Demanem als clients que volen dinar
    if comanda_per_dinar > 0: # Si la comanda es més gran que 0 continuarà en el bucle
        preutotal += preu[comanda_per_dinar - 1] # Per quadrar el número de la llista


    elif comanda_per_dinar == 0: # Si la comanada es 0
        print("Import total", preutotal, "€") # Imprimir l'import total
        break #Sortir del bucle