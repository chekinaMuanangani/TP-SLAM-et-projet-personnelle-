id = input("Crée un identifiant:")
mdp = input("Crée un mot de passe:")
dict(mot_de_passe=mdp, identifiant=id )
if len(mdp)<9:
    print("mot de passe trop cours")
else : 
    print("Identifiant et mot de passe créés avec succès.")
#Demande a l'utilisateur de confirmer son identifiant et mot de passe
confirme_id = input("confirmer votre identifiant :")
while confirme_id != id:
    print("id incorrect")
    break
confirme_mdp = input("confirmer votre mot de passe:")
while confirme_mdp !=mdp :
    print("mdp incorrect")
    break
else:
    print("="*33)
    print(f"Bonjour,{confirme_id} !")
    print("="*33)
