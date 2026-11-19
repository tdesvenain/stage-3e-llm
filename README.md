# Stage de 3e : fabriquer un jeu avec une IA

Bienvenue ! Cette semaine, tu vas découvrir comment un développeur travaille avec un
grand modèle de langage (un **LLM**, la technologie derrière ChatGPT) et fabriquer ton
propre jeu d'aventure qui discute avec toi.

## Les règles d'or

1. **La clé secrète ne va jamais dans le code.** Elle vit dans le fichier `.env`, que git
   ignore. Si tu la vois quelque part ailleurs, préviens ton encadrant.
2. **L'IA se trompe.** Elle prédit des mots probables, elle ne « sait » rien. Essaie de la
   piéger, c'est le meilleur moyen de comprendre comment elle marche.
3. **L'IA raconte, le code décide.** Les règles du jeu (la vie, les objets, les lieux)
   vivent dans ton code Python. L'IA met en scène ce que le code a décidé.
4. **On avance par petits pas.** Un script qui marche, puis une amélioration, puis un
   commit. Jamais trois changements à la fois.

## Installation (une seule fois)

Ouvre un terminal dans ce dossier, puis :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Ensuite, ton encadrant remplit la clé dans `.env`.


----------------------------------------------------------------------------------------------------------------------------------


## Ce que tu as au départ

| Fichier | Ce qu'il fait |
|---|---|
| `00_echauffement.py` | Un mini-chatbot sans IA, à construire ensemble en six étapes. |
| `01_bonjour.py` | Pose une question au modèle, affiche la réponse. Dix lignes. |
| `02_personnage.py` | Discute avec un personnage que tu inventes. Prompt système, mémoire, température. |
| `interface.py` | Les trois fonctions qui parlent au terminal : `afficher`, `demander`, `patienter`. |
| `afficher_image.py` | Affiche une image en pixel art dans le terminal. Zéro IA. |
| `PYTHON.md` | L'aide-mémoire des sept briques Python du jeu. Garde-le ouvert. |

Lance un script avec :

```bash
python 00_echauffement.py
```

## Les objectifs de la semaine

Ton jeu part du script 2 et grandit chaque jour d'un mécanisme. À toi de choisir
l'univers, le personnage et l'histoire.

- **Jour 1.** Un personnage garde un secret (un lieu, une adresse). Le joueur doit le convaincre de
  le révéler, puis taper `aller <secret>` pour gagner. Tu apprends : le prompt système, la boucle de
  conversation, du texte qui devient une décision du code.
- **Jour 2.** Le joueur a des points de vie et un inventaire. Un objet est caché quelque part, il
  faut fouiller au bon endroit pour le trouver. Tu apprends : l'état du jeu dans un dictionnaire
  Python, un protocole entre l'IA et le code.
- **Jour 3.** L'objet trouvé sert à quelque chose : une clé ouvre une porte. L'IA comprend des
  phrases libres et les traduit en actions que le code vérifie. Tu apprends : l'IA comme interprète,
  le code comme arbitre.
- **Jour 4.** Un lieu avec plusieurs salles et une carte. Le code sait toujours où est le joueur.
  Tu apprends : un graphe de salles, l'autocomplétion des sorties possibles.
- **Jour 5.** Une image pixel art par lieu, les finitions, la démo à l'équipe. Tu apprends : présenter
  ton travail.

## Le terminal, c'est dans `interface.py`

Le script 2 n'utilise jamais `print` ni `input` directement : il appelle `afficher`,
`demander` et `patienter` dans `interface.py`. C'est le seul fichier qui parle au
terminal. Ouvre-le, change une couleur, relance le jeu. Plus tard, tu pourras y remplacer
`input()` par `prompt_toolkit` (historique avec les flèches, autocomplétion des actions
possibles) sans toucher une ligne du jeu.

Pour afficher une de tes illustrations (80 caractères de large par défaut) :

```bash
python afficher_image.py images/pirate.png 60
```

Depuis le jeu, `from afficher_image import afficher_image` puis `afficher_image("images/pirate.png")`
à l'entrée dans un lieu. Range tes images dans un dossier `images/` avec des noms parlants.

## Expériences à tenter

- Dans `02_personnage.py`, change `PERSONNALITE` : pirate, prof grincheux, robot qui ne
  parle qu'en rimes. Puis monte la `TEMPERATURE` à 1.5 et regarde ce qui se passe.
- Demande au personnage la date d'aujourd'hui, un calcul compliqué, ou un fait sur un
  village minuscule. Trouve-le en train d'inventer.
- Essaie de lui faire révéler son secret par la ruse. Note ce qui marche. Puis renforce
  son prompt et recommence.
- Quand une amélioration marche, fais un commit avec ton encadrant.
