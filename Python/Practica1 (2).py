DNI=input("Quin es el teu DNI? ") #Número DNI
preu=float(input("Quin es el preu d'algun dels productes que has comprat? ")) #Preu
descompte=float(input("Aquest es el tant per cent de descompte: ")) #Preu inserit
preudescompte=preu*descompte/100 #Descompte
preutotal=preu-preudescompte #Preu amb descompte
iva=float(input("Quin es el número d'IVA? ")) #Espai per inserir l'IVA
ivatotal=preutotal*iva/100 #Calcul IVA aplicat
print("Aquest es l'IVA aplicat: " , ivatotal) #IVA inserit
preufinal=preutotal+ivatotal #Preu amb descompte més IVA inserit
print("Aquest es el preu final: " , preufinal) #Preu final
lletra="TRWAGMYFPDXBNJZSQVHLCKE" #lletra DNI
print("El teu DNI es: " , DNI , lletra[int(DNI)%23]) #Calcul DNI amb lletra
