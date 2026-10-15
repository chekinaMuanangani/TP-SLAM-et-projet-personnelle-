# CODE PIN MARC 
code_pin =4567
inser_code = int(input("Entrez votre code pin :"))
if code_pin == inser_code:
    print("Code correcte")
else :
    print("Code incorrecte")

#Signe d'un numbre
nb_entier = int(input("Entrez un nombre entier :"))
if nb_entier >= 1:
    print("Positif")
elif nb_entier == 0:
 print("Nul")
else:
   print("Négatif")

#Parité
nb_entier = int(input("Entrez un nombre entier :"))
if nb_entier % 2 == 0 :
   print(f"{nb_entier} est un nombre pair")
else:
   print(f"{nb_entier} est un nombre impair")

#AGE
age =int(input("Entrez votre âge :"))
if age <= 12:
   print(f"A {age} ans, vous êtes un enfant.")
elif 12 < age > 18 :
   print(f"A {age} ans, vous êtes un adolescent")
else:
   print(f"A {age} ans, vous êtes un adulte")

#PERTE OU PROFIT 
prix_prod = float(input("Entrez le prix de production :"))
prix_vente = float(input("Entrez le prix de vente :"))
if prix_vente < prix_prod :
    print("Perte")
else:
    print("Profit")

#Maximum
pre_nb = float(input("Entrez le premier nombre :"))
scd_nb = float(input("Entrez le second nombre :"))
troi_nb = float(input("Entrez le troisieme nombre :"))
if scd_nb < pre_nb > troi_nb :
    print(f"Le maximum est le premier nombre :{pre_nb} ")
elif pre_nb < scd_nb > troi_nb :
    print(f"Le maximum est le second nombre{scd_nb}")
elif pre_nb < troi_nb > scd_nb :
    print (f"Le maximum est le troisième nombre{troi_nb}")  

#Triangle Rectangle 
print("Entrez les valeurs dans l'ordre croissant svp")
cote_1 = float(input("côté 1:"))
cote_2 = float(input("côté 2:"))
cote_3 = float(input("côté 3:"))
if cote_1 > cote_2 > cote_3 :
    sum = float(cote_1**2 + cote_2**2)
    if sum == cote_3**2:
        print("triangle rectangle")
    else :
        print("triangle non rectangle")
else:
    print("Erreur les nombre entrez ne sont pas dans l'ordre croissant")

# STRUCTURE ALT PARTIE 2
#Année bissextile
anne = int(input("Saisir l'année :"))
if(anne %4 ==0 and anne %400):
    print("Année bissextile")
elif(anne %100 !=0):
    print("Année non bissextile")
else:
    print("Année non bissextile")

#société de transport
age = int(input("Saisir votre âge :"))
prix = 10
if (age <=  5):
    print(f"Le voyage est gratuit")
elif(age >5 and age < 16):
    tarif_mineur = prix*0.5
    print(f"Le prix est de {tarif_mineur}€")
elif(age < 21 and age > 16):
    tarif_ado = prix * 0.6
    print(f"Le prix est de {tarif_ado}€")
elif(age > 21 and age < 51):
    print(f"Le prix est de {prix}€")
elif(age >= 51):
    tarif_senior = prix *0.9
    print(f"Le prix est de {tarif_senior}€")

# VOYAGE SCOLAIRE 
eleve = int(input("Entrez nombre d'élève :"))
duree = int(input("Entrez la durée du voyage :"))
nourriture = 3.50 * duree
if (eleve >=25):
    transport = 110.00
else :
    transport = 100.00
if (eleve < 20):
    hebergement = 4.50
    prix = hebergement * duree + nourriture + transport
    print(f"nombre d'élève :{eleve}")
    print(f"Durée du voyage :{duree} jours")
    print(f"Le prix du voyage est de {prix}€ par élève")
elif (35 < eleve > 20 ):
    hebergement = 3.80 
    prix = hebergement * duree+ nourriture + transport
    print(f"nombre d'élève:{eleve}")
    print(f"Durée du voyage:{duree} jours")
    print(f"Le prix du voyage est de {prix}€ par élève")
elif (eleve > 35 ):
    hebergement = 4.00
    prix = hebergement * duree+ nourriture + transport
    print(f"nombre d'élève:{eleve}")
    print(f"Durée du voyage:{duree} jours")
    print(f"Le prix du voyage est de {prix}€ par élève")

#VINCI LOCATION     