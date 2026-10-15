#version sans f-string
#Entre c'est information personnel 
nom_utilisateur = input("Entrez votre nom :")
prenom_utilisateur = input("Entrez votre prenom :")
adresse_mail = input("Entrez votre adresse mail:")
num = int(input("Entrez votre numero de tel : "))
post = input("Quel poste recherchez vous ? :")
nom_entreprise = input("Quel entreprise cible vous ? :")
# generation du mail 
print("Bonjour je m'appel ", prenom_utilisateur, nom_utilisateur)
print("Je cherche un poste dans le " , post "dans l'entreprise", nom_entreprise)
print("Pour me contacter voici mon mail:", adresse_mail,"et mon numero de telephone:", num)
