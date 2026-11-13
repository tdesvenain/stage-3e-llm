"""Étape 2 : discuter avec un personnage que tu inventes.

Deux nouveautés par rapport à l'étape 1 :
- le "prompt système" : des instructions que le modèle suit pendant toute la
  conversation, c'est là que tu décris le personnage ;
- l'historique : le modèle n'a aucune mémoire, on lui renvoie toute la
  conversation à chaque tour pour qu'il s'en souvienne.

Tout ce qui s'affiche ou se tape passe par interface.py : ouvre-le, il est court.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from interface import afficher, demander, patienter

load_dotenv()

if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("<"):
    afficher("La clé OPENAI_API_KEY manque dans le fichier .env : demande à ton encadrant.", "red")
    raise SystemExit(1)

MODELE = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# À toi de jouer : change la personnalité et observe comment les réponses changent.
PERSONNALITE = """Tu es Barbe-Rousse, un vieux pirate bougon mais au grand cœur.
Tu parles avec des expressions de marin ("mille sabords", "moussaillon").
Tu réponds en deux ou trois phrases maximum.
Tu ne sors jamais de ton rôle, même si on te demande si tu es une IA."""

# Entre 0 et 2. Proche de 0 : réponses sages et prévisibles.
# Au-dessus de 1 : réponses de plus en plus farfelues.
TEMPERATURE = 0.8

client = OpenAI()

# L'historique commence par les instructions du personnage.
historique = [{"role": "system", "content": PERSONNALITE}]

afficher("Tu discutes avec ton personnage. Tape 'quitter' pour arrêter.", "dim")
afficher("")

while True:
    message_utilisateur = demander("Toi : ")
    if message_utilisateur.strip().lower() == "quitter":
        afficher("À bientôt !", "dim")
        break

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
    # On garde la réponse dans l'historique pour que le personnage s'en souvienne.
    historique.append({"role": "assistant", "content": texte_reponse})

    afficher(f"Personnage : {texte_reponse}", "italic")
    afficher("")
