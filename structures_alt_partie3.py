#Nation 
sceance = int(input("Entrez le nombre de scéance :"))
tarif_A = 145 + 10.50 * sceance
tarif_b = 15.50 * sceance
print(f"Nombre de scéance : {sceance}")
if (tarif_A > tarif_b):
    print(f"Pour {sceance}, le tarif B est plus avantageux.")
elif (tarif_A < tarif_b) :
    print(f"Pour {sceance}, le tarif A est plus avantageux.")
else : 
    print(f"Pour {sceance}, aucun tarif n'est plus avantageux que l'autre.")
detail = input("Souhaitez-vous plus de détails? (yes/no) :")
if detail == "yes" or "no" :
    print(f"Tarif A : {tarif_A} euros")
    print(f"Tarif B : {tarif_b} euros")

#Voyelle, consonne ou caractère spécial
ch = input("Entrez un charactère :")
if len(ch) != 1 :
    print("Entrez un seul charactère")
else :
    if (ch == "a" or ch == "e" or ch == "i" or ch ==  "o" or ch == "y" or ch == "A" or ch == "E"  or ch == "I" or ch == "O" or "Y")
     print(f"{ch} : voyelle")
    elif ( ch >= "a" and ch == "z") or (ch >="A" and ch <= "Z"): 
        print(f"{ch} : consonne ")
    else:
        print(f"{ch} : charactère spécial")

#facture
prix :float(intput("Saisir le pix de votro produit :"))
if (prix >= 5000):
    prix_ht = prix * 0.5
elif (5000 < prix >= 2000):
    prix_ht = prix * 0.3 
elif (2000 < prix >=1000):
    prix_ht=prix * 0.1
elif (prix > 1000):
     