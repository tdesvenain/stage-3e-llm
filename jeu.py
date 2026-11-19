"""Étape 2 : discuter avec un personnage que tu inventes.

Deux nouveautés par rapport à l'étape 1 :
- le "prompt système" : des instructions que le modèle suit pendant toute la
  conversation, c'est là que tu décris le personnage ;
- l'historique : le modèle n'a aucune mémoire, on lui renvoie toute la
  conversation à chaque tour pour qu'il s'en souvienne.

Tout ce qui s'affiche ou se tape passe par interface.py : ouvre-le, il est court.
"""
import copy
import os
from rich.console import Console
from dotenv import load_dotenv
from openai import OpenAI

from interface import afficher, demander, patienter
from afficher_image import afficher_image
from prompt import PERSONNALITE
from prompt import PERSONNALITE1

load_dotenv()

import ast
debut = "<<<GAME_STATE_START>>>"
fin = "<<<GAME_STATE_END>>>"


game_state = {
    "island": 2,
    "location": "house",
    "lives": 1,
    "health":100,
    "inventory": ["pc"],
    "pc_connected": False,
    "usb_connected": False,
    "briefcase_opened": False,
    "game_won": False
}


if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("<"):
    afficher("La clé OPENAI_API_KEY manque dans le fichier .env : demande à ton encadrant.", "red")
    raise SystemExit(1)

MODELE = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


# Entre 0 et 2. Proche de 0 : réponses sages et prévisibles.
# Au-dessus de 1 : réponses de plus en plus farfelues.
TEMPERATURE = 0.8

client = OpenAI()

# L'historique commence par les instructions du personnage.
historique = [{"role": "system", "content": PERSONNALITE}]

afficher("Tu discutes avec Emmanuel. Essaye de découvrir son secret. Tape 'quitter' pour arrêter.", "dim")
afficher("")
debug_mode = False
quete_fini = "*"
indicateur_quete = False
debut_game = True 
while True:
    ancien_ile = game_state.get("island")
    ancien_lieu = game_state.get("location")
    if debug_mode == True:
        print(f"Debug mode on, game state : {game_state}\nThe Emmanuel quest is at state : {indicateur_quete}\nThe start game is at state : {debut_game}\n")
    if debut_game == False:
        message_utilisateur = demander("Toi : ")
    elif debut_game == True:
        message_utilisateur = "bonjour"
        debut_game = False
    if message_utilisateur.strip().lower() == "quitter":
        afficher("À bientôt !", "dim")
        break
    if message_utilisateur.strip().lower() == "debugon":
        debug_mode = True
        print("Debug mode on")
    if message_utilisateur.strip().lower() == "debugoff":
        debug_mode = False
        print("Debug mode off")
    historique.append({"role": "user", "content": message_utilisateur})

    try:
        with patienter("Le personnage réfléchit…"):
            reponse = client.chat.completions.create(
                model=MODELE,
                messages=historique,
                temperature=TEMPERATURE,
            )
    except Exception as erreur:
        afficher(f"Oups, l'appel au modèle a échoué : {erreur}", "red")
        historique.pop()  # on retire le message qui n'a pas eu de réponse
        continue
   

    texte_reponse = reponse.choices[0].message.content

    #if indicateur_quete == True:
    if (debut in texte_reponse) and (fin in texte_reponse):
        narration, reste = texte_reponse.split(debut, 1)
        donnees, _ = reste.split(fin, 1)
        game_state = ast.literal_eval(donnees.strip())
        texte_final = narration.strip()
    else:
        texte_final = texte_reponse

    historique.append({"role": "assistant", "content": texte_reponse})

    afficher(f"Personnage : {texte_final}", "italic")
    afficher("")
   
    if quete_fini in texte_reponse:
        indicateur_quete = True
        historique = [{"role": "system", "content": PERSONNALITE1}]

    statut_localisation = game_state.get("location")
    statut_ile = game_state.get("island")

    if statut_ile != ancien_ile:
        print(statut_ile, ancien_ile)
        if statut_ile == 1:
            if statut_localisation != "island_center":
                afficher_image("./Monde/images/Ile.png")
        elif statut_ile == 2:
            afficher_image("./Monde/images/Ile.png")
        elif statut_ile == 3:
            if statut_localisation != "router":
                afficher_image("./Monde/images/Ile.png")

    if statut_localisation != ancien_lieu:
        if statut_localisation == "house":
            afficher_image("./Monde/images/Maison.png")
        elif statut_localisation == "island_center":
            afficher_image("./Monde/images/Ile.png")
        elif statut_localisation == "well":
            afficher_image("./Monde/images/Puit.png")
        elif statut_localisation == "building_1":
            afficher_image("./Monde/images/Batiment.png")
        elif statut_localisation == "building_2":
            afficher_image("./Monde/images/Batiment.png")
        elif statut_localisation == "building_3":
            afficher_image("./Monde/images/Batiment.png")
        elif statut_localisation == "building_4":
            afficher_image("./Monde/images/Batiment.png")
        elif statut_localisation == "bridge_1_2":
            afficher_image("./Monde/images/Pont.png")
        elif statut_localisation == "bridge_1_3":
            afficher_image("./Monde/images/Pont.png")
        elif statut_localisation == "bridge_2_3":
            afficher_image("./Monde/images/Pont.png")
        elif statut_localisation == "router":
            afficher_image("./Monde/images/Internet.png")

    if debug_mode == True:
        print(f"Debug mode end : User is at {statut_localisation} before it was at {ancien_lieu}\nUser is at island {statut_ile} before it was at {ancien_ile}\n")