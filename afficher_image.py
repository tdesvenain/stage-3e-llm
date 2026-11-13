"""Afficher une image dans le terminal, en "pixel art".

L'idée : le terminal ne sait afficher que des caractères, mais il sait les colorer.
On réduit l'image à quelques dizaines de pixels de large, puis pour chaque colonne on
prend les pixels deux par deux (celui du haut et celui du bas) et on affiche le
caractère ▀ (demi-bloc haut) : sa couleur de texte = le pixel du haut, sa couleur de
fond = le pixel du bas. Un caractère affiche donc deux pixels, ce qui compense le fait
qu'un caractère est deux fois plus haut que large.

Utilisation seule :      python afficher_image.py images/pirate.png
Depuis le jeu :          from afficher_image import afficher_image
                         afficher_image("images/pirate.png", largeur=60)
"""

import sys

from PIL import Image

DEMI_BLOC_HAUT = "▀"
REINITIALISER = "\033[0m"  # code qui remet les couleurs du terminal à la normale


def couleur_ansi(rouge, vert, bleu, fond=False):
    """Fabrique le code ANSI qui colore le texte (ou le fond) en vraie couleur 24 bits."""
    numero = 48 if fond else 38  # 38 = couleur du texte, 48 = couleur du fond
    return f"\033[{numero};2;{rouge};{vert};{bleu}m"


def afficher_image(chemin, largeur=80):
    """Affiche l'image dans le terminal, sur `largeur` caractères de large."""
    image = Image.open(chemin).convert("RGB")

    # On garde les proportions : la hauteur en pixels suit la largeur demandée.
    # Hauteur paire obligatoire, puisqu'on empile les pixels deux par deux.
    hauteur = round(image.height * largeur / image.width)
    if hauteur % 2 == 1:
        hauteur += 1
    image = image.resize((largeur, hauteur))

    lignes = []
    for y in range(0, hauteur, 2):  # on avance de deux pixels à la fois
        ligne = []
        for x in range(largeur):
            pixel_haut = image.getpixel((x, y))
            pixel_bas = image.getpixel((x, y + 1))
            ligne.append(couleur_ansi(*pixel_haut) + couleur_ansi(*pixel_bas, fond=True) + DEMI_BLOC_HAUT)
        lignes.append("".join(ligne) + REINITIALISER)

    print("\n".join(lignes))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python afficher_image.py <fichier image> [largeur]")
        raise SystemExit(1)

    largeur_demandee = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    afficher_image(sys.argv[1], largeur_demandee)
