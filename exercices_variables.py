import math

# Exercice : Générer un mail de contact pour une recherche d'emploi

# Énoncé :
# Écrivez un script Python qui collecte des informations personnelles et professionnelles auprès de l'utilisateur,
# puis génère automatiquement un texte de mail de contact pour une candidature spontanée.
# Le mail doit inclure les informations suivantes :
# - Nom et prénom de l'utilisateur
# - Adresse email et numéro de téléphone
# - Poste recherché
# - Nom de l'entreprise cible

# Votre script doit :
# 1. Utiliser des f-strings pour générer le texte du mail.
# 2. Générer le même texte de mail sans utiliser les f-strings (en concaténant les chaînes de caractères).
# 3. Afficher les deux versions du mail généré.

# Script pour collecter des renseignements et générer un mail de contact pour une recherche d'emploi

# ----------------- Collecte des renseignements auprès de l'utilisateur------------------


# ----------------- Génération du texte du mail ------------------


# ----------------- Affichage du mail généré ------------------

# ----------------- Génération du texte du mail sans utiliser f-strings ------------------

# ----------------- Affichage du mail généré ------------------



# ----------------- EXERCICES DE MANIPULATION DE NOMBRES -----------------
# Voici quelques exercices pour pratiquer la manipulation de nombres en Python.
# Complétez le code ci-dessous pour afficher la somme de deux nombres de deux façons différentes
# 1. En utilisant des f-strings
# 2. En concaténant les chaînes de caractères
x= 10
y= 5
z= x + y
print(z)
print(f"le résulta est{z}")


# Voici quelques exercices pour pratiquer la manipulation de chaînes de caractères en Python.
# Complétez le code ci-dessous pour afficher une phrase de deux façons différentes
phrase = "Bonjour, je m'appelle John."


# Voici quelques exercices pour pratiquer la manipulation de types de données en Python.
# afficher le type des différentes variables suivantes : x y z phrase email telephone


# Voici quelques exercices pour pratiquer la saisie utilisateur en Python.
# Complétez le code ci-dessous pour demander à l'utilisateur son nom et son âge,
nom_utilisateur = input("Entrez votre prénom: ")
age_utilisateur = input("Entrez votre âge: ")
age_utilisateur = int(input("Entrez votre âge: ")) # conversion de age_utilisateur en entier

# puis afficher un message personnalisé avec son nom et l'année de naissance.
annee_naissance =int(input(f"Bonjour {nom_utilisateur} vous etes nee en {annee_naissance}"))


# ----------------- EXERCICES DE MANIPULATION DE VARIABLES -----------------

# Exercice 1 : Échange de valeurs
# Échangez les valeurs de deux variables a et b, puis affichez-les.
a = 5
b = 10
b = a
a = b
print(a, b)



# Exercice 2 : Calcul de la moyenne
# Calculez la moyenne de trois nombres donnés.
a, b, c = 4, 8, 12
moyenne = np.mean(a,b,c)

# Exercice 3 : Conversion Celsius en Fahrenheit
# Convertissez une température donnée en Celsius en Fahrenheit.
celsius = 25
fahrenheit = (celsius*9/5)+32


# Exercice 4 : Calcul de l'aire d'un rectangle
# Calculez l'aire d'un rectangle à partir de sa longueur et de sa largeur.
longueur = 7
largeur = 3
aire = longueur * largeur

# Exercice 5 : Calcul du périmètre d'un cercle
# Calculez le périmètre d'un cercle à partir de son rayon.
# attention : vous aurez besoin de la constante math.pi pour cela (import math)
rayon = 5
perimetre = 2 * math.i * rayon

# Exercice 6 : Inversion de chaîne
# Inversez une chaîne de caractères donnée.
chaine = "Python"
reversed(chaine)


# Exercice 7 : Calcul de la puissance
# Calculez la puissance d'un nombre donné (exemple : 2^3).
# affichez le résultat
base = 2
exposant = 3
puissance = base ** exposant


# Exercice 8 : Vérification de la présence d'un mot
# Vérifiez si un mot donné est présent dans une phrase.
# affichez le résultat (True/False)
# en deux lignes de code

phrase = "Bonjour tout le monde"
mot = "tout"
bool(mot)


# Exercice 9 : Calcul du reste
# Calculez le reste de la division de deux nombres.
# affichez le résultat
dividende = 17
diviseur = 4
division = float(dividende / diviseur)


# Exercice 10 : Conversion en majuscules
# Convertissez une chaîne de caractères en majuscules.
chaine = "hello world"
chaine_maj = chaine.upper()

# Exercice 11 : Conversion en minuscules
# Convertissez une chaîne de caractères en minuscules.
chaine = "HELLO WORLD"
chaine_min =chaine.lower()

# Exercice 12 : Remplacement de caractères
# Remplacez un mot dans une phrase par un autre mot.
phrase = "J'aime Python"
nouvelle_phrase = phrase.replace("J'aime la vie")

# Exercice 13 : Calcul du carré d'un nombre
# Calculez le carré d'un nombre donné.
# affichez le résultat
nombre = 6
carre = nombre **2
print(carre)

# Exercice 14 : Extraction de sous-chaîne
# Extrayez une sous-chaîne d'une chaîne donnée "progr".
# affichez le résultat
# attention : les indices commencent à 0 en Python
# par exemple, pour "Programmation", l'indice 0 correspond à "P"

chaine = "Programmation"
sous_chaine = s[0:4]

# Exercice 15 : Arrondi d'un nombre flottant
# Arrondissez un nombre flottant à l'entier le plus proche.
# affichez le résultat
nombre_flottant = 3.7
nombre_arrondi = round(nombre_flottant)

# Exercice 16 : Vérification de la longueur d'une chaîne
# Vérifiez si une chaîne contient plus de 10 caractères.
# affichez le résultat 
chaine = "Bonjour"
longueur_sup_10 = bool(len(chaine) < 10 )
print(longueur_sup_10)

# Exercice 17 : Conversion d'une chaîne en liste
# Convertissez une chaîne de caractères en une liste de mots.
chaine = "Apprendre Python est amusant"
liste_mots = ["Apprendre", "Python", "est", "amusant"]

