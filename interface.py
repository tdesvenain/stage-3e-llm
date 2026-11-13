"""Le seul fichier où le jeu parle au terminal.

Trois fonctions, et le reste du jeu ne sait pas quelle bibliothèque est derrière :
- afficher(texte, style) : écrire du texte, avec une couleur si on veut ;
- demander(invite) : poser une question au joueur et renvoyer sa réponse ;
- patienter(message) : montrer une petite animation pendant qu'on attend l'IA.

Aujourd'hui la saisie est un simple input(). Plus tard, on pourra la remplacer par
prompt_toolkit (historique avec les flèches, autocomplétion des actions) sans toucher
au reste du jeu : c'est tout l'intérêt d'avoir regroupé ça ici.
"""

from rich.console import Console

console = Console()


def afficher(texte, style=None):
    """Affiche du texte. `style` est une couleur ou un style rich : "red", "bold yellow", "italic"."""
    console.print(texte, style=style, highlight=False)


def demander(invite):
    """Affiche l'invite en couleur, puis attend la réponse du joueur."""
    console.print(f"[bold cyan]{invite}[/]", end="")
    return input()


def patienter(message):
    """À utiliser avec `with` : affiche une animation tant que le bloc n'est pas fini."""
    return console.status(f"[dim]{message}[/]", spinner="dots")
