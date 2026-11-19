"""Étape 1 : poser une question au modèle et afficher sa réponse.

Tout l'appel tient en quelques lignes. Lis-les dans l'ordre : on charge la clé,
on crée un client, on envoie un message, on affiche ce qui revient.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # lit le fichier .env et place la clé dans les variables d'environnement

if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("<"):
    print("La clé OPENAI_API_KEY manque dans le fichier .env : demande à ton encadrant.")
    raise SystemExit(1)

MODELE = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI()  # la clé est lue automatiquement dans OPENAI_API_KEY

   
def openai(question):
    reponse = client.chat.completions.create(
        model=MODELE,
        messages=[{"role": "user", "content": question}],
    )
    return reponse 

#liste_questions = []

#while True :
#question = input("Pose ta question : ")
#if question == "break" :
#break
#else:
#questions = f"Tu est une ia qui tourne sur python, voici la listes des ancien prompt de l'utilisateur :{liste_questions} maintenant repond a la question de l'utilisateur qui sera après les 2 2 points ::" + question
#reponse_openai = openai(questions)
#print()
#print(reponse_openai.choices[0].message.content)
#liste_questions.append(question)  

liste_questions = {}

while True :
 question = input("Pose ta question : ")
 if question == "break" :
  break
 else:
   questions = f"Tu est une ia qui tourne sur python, voici la listes des ancien prompt de l'utilisateur et de tes reponses :{liste_questions} maintenant repond a la question de l'utilisateur qui sera après les 2 2 points ::" + question
   reponse_openai = openai(questions)
   print()
   print(reponse_openai.choices[0].message.content)
   liste_questions[question] = reponse_openai  


   
