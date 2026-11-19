"""Échauffement : un mini-chatbot SANS intelligence artificielle.

On le construit ensemble en six étapes de dix minutes. À chaque étape, tu ajoutes une
brique de Python. À la fin, tu auras écrit toi-même la boucle de conversation que le
jeu utilise toute la semaine... et tu auras joué le rôle du LLM avec tes réponses
toutes faites. Demain, le script 01 remplace tes réponses par une vraie IA.

Lance-le à chaque étape pour voir ce qui change :  python 00_echauffement.py
"""

# ÉTAPE 1 : une variable, print() et input()
# But : le programme demande ton prénom et te salue.
# Briques : une variable (une boîte avec un nom), input() qui lit ce qu'on tape,
#           print() qui affiche, et f"..." pour glisser une variable dans du texte.
prenom = input(f"Quel est ton prénom ?\n")
print(f"Enchanté {prenom}\n")


# ÉTAPE 2 : une boucle while
# But : le programme te pose la question "Toi : " encore et encore, jusqu'à ce que tu
#       tapes "quitter".
# Briques : while True: pour répéter, break pour sortir, == pour comparer.
while True :
  print("toi")
  demande_quit = input("Dit break pour arreter\n")
  if demande_quit == "break":
    break 


# ÉTAPE 3 : if / elif / else
# But : le personnage répond différemment selon ce que tu dis. S'il y a "bonjour" dans ton
#       message, il salue ; s'il y a "trésor", il bougonne ; sinon il dit qu'il n'a pas compris.
# Briques : if, elif, else, et le mot in pour chercher un mot dans un texte.
utilisateur_input = input("Parle au personage\n")
if utilisateur_input == "bonjour":
 print(f"bonjour {prenom} ravi de faire ta connaisance")
elif utilisateur_input == "trésor":
 print("grrrrr")
else :
 print("je n'ai pas compris")


# ÉTAPE 4 : un dictionnaire
# But : au lieu d'empiler des elif, toutes les réponses sont rangées dans un dictionnaire
#       mot-clé → réponse. Ajouter une réponse, c'est ajouter une ligne.
# Briques : {"clé": "valeur"}, et for ... in ....items() pour parcourir toutes les paires.
Dico = {"clé": "valeur"}

for k, v in Dico.items():
    print(k, v)

# ÉTAPE 5 : une liste
# But : le joueur peut taper "prendre torche" : la torche va dans son inventaire. Taper
#       "inventaire" l'affiche.
# Briques : une liste [], .append() pour ajouter, ", ".join() pour afficher.
interaction_inventaire = input("inventaire\n")
inventaire = []
if interaction_inventaire == "prendre torche":
  inventaire.append("torche")
elif interaction_inventaire == "inventaire":
  print(inventaire)
  


# ÉTAPE 6 : une fonction
# faire une boucle qui permet à l'utilisateur de parler au personnage
# gérer le fait de quitter comme à l'étape 2
# on reprend les conditions de l'étape 3 mais la réponse est retournée par une fonction
# le print est fait après l'appel de la fonction
# But : toute la logique "trouver la bonne réponse" est rangée dans une fonction
#       repondre(message) qui renvoie le texte à afficher. La boucle devient toute petite.
# Briques : def, return, et appeler la fonction.
def bot(utilisateur_input):
  if utilisateur_input == "bonjour":
    return "bonjour {prenom} ravi de faire ta connaisance"
  elif utilisateur_input == "trésor":
    return "grrrrr"
  else :
    return "je n'ai pas compris"
  
liste_questions = []

while True :
 demande_user = input()
 
 if demande_user == "break":
  break
 else:
  demande_user = f"Tu est une ia qui tourne sur python, voici la listes des ancien prompt de l'utilisateur :{liste_questions} maintenant repond a la question de l'utilisateur qui sera après les 2 2 points ::" + demande_user 
  reponse = bot(demande_user)
  print(reponse)
  liste_questions.append(reponse)  


