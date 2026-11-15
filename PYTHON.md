# Aide-mémoire Python

Tout le jeu tient avec ces sept briques. Les exemples viennent du jeu lui-même.

## 1. Une variable : une boîte avec un nom

```python
MODELE = "gpt-4o-mini"
vie = 10
vie = vie - 2          # la boîte contient maintenant 8
```

## 2. Afficher et lire : print() et input()

```python
print("Bienvenue dans le château hanté.")
action = input("> ")                    # attend que le joueur tape quelque chose
print(f"Tu as dit : {action}")          # f"..." glisse une variable dans le texte
```

Dans le jeu, à partir du script 2, on passe par `afficher()` et `demander()` de `interface.py`,
qui font la même chose en couleur.

## 3. Décider : if / elif / else

```python
if action == "quitter":
    print("À bientôt !")
elif "pot" in action:                   # in : le mot "pot" est-il quelque part dans action ?
    print("Tu fouilles le pot...")
else:
    print("Je n'ai pas compris.")
```

L'indentation (les espaces au début de la ligne) dit ce qui est « dedans ». Elle compte vraiment.

## 4. Une liste : plusieurs choses dans l'ordre

```python
objets = ["torche"]
objets.append("clé rouillée")           # ajouter à la fin
if "clé rouillée" in objets:            # est-ce que je l'ai ?
    print("Tu as la clé !")
print(", ".join(objets))                # "torche, clé rouillée"
```

## 5. Un dictionnaire : des paires clé → valeur

```python
joueur = {"vie": 10, "objets": ["torche"], "lieu": "cuisine"}
print(joueur["vie"])                    # 10
joueur["lieu"] = "cave"                 # changer une valeur

sorties = {"cuisine": ["cave", "couloir"], "cave": ["cuisine"]}
print(sorties["cuisine"])               # ["cave", "couloir"]

for mot_cle, reponse in reponses.items():   # parcourir toutes les paires
    if mot_cle in message:
        print(reponse)
```

C'est la brique la plus importante du jeu : l'état du joueur, les cachettes et la carte sont des
dictionnaires.

## 6. Répéter : while

```python
while True:                             # pour toujours...
    action = input("> ")
    if action == "quitter":
        break                           # ...sauf si on sort avec break
    print("Tu fais :", action)
```

## 7. Une fonction : un bout de code avec un nom

```python
def description_etat():
    objets = ", ".join(joueur["objets"])
    return f"vie={joueur['vie']} objets={objets}"    # return : ce que la fonction renvoie

texte = description_etat()              # on l'appelle, on récupère le résultat
```

## Et aussi

- `import` : aller chercher du code écrit par d'autres. `from interface import afficher`.
- `try` / `except` : essayer quelque chose qui peut échouer (un appel à l'API) et réagir si ça rate.
- Un message d'erreur se lit **de bas en haut** : la dernière ligne dit quoi, celle du dessus dit où.
