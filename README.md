# RPG Senegal - Projet POO Python

## Presentation

Pour ce projet on a choisi de creer un systeme de combat RPG base sur les royaumes historiques du Senegal.
Les heros sont de grands rois et resistants senegalais qui combattent des creatures mystiques du folklore africain.
Le projet utilise les concepts de la Programmation Orientee Objet : les classes, les attributs, les methodes, l'heritage et le polymorphisme.

## Comment lancer le jeu


```
python main.py
```

Tous les fichiers doivent etre dans le meme dossier.

## Structure du projet

- creature.py : classe de base Creature dont heritent Personnage et Monstre
- personnage.py : classe Personnage avec ses attributs et la liste des heros
- monstre.py : classe Monstre avec ses resistances et la liste des monstres
- arme.py : classe Arme et les armes disponibles
- action.py : les actions du combat et nos deux ameliorations
- utils.py : fonctions utilitaires pour les des, les menus et la saisie
- main.py : boucle principale du jeu

## Les heros

- Lat Dior : guerrier du Cayor, attaque forte, arme tranchante
- Aline Sitoe Diatta : pretresse de Casamance, specialiste des soins, arme percante
- Maba Diakhou Ba : chef religieux, renforce ses allies, arme de feu
- Omar Foutiyou Tall : leader spirituel, puissant en magie, arme magique
- Samory Toure : grand stratege, inflige beaucoup de degats, arme contondante

## Les monstres

- Mami Wata : esprit de l'eau, peut empoisonner les heros, resiste au magique
- Esprit du Fleuve Senegal : resiste au tranchant
- Serpent d'eau : resiste au percant
- Djinn de la mer : resiste au percant
- Ombre des profondeurs : resiste au magique
- Poisson demoniaque : resiste au tranchant

## Ce qu'on a respecte dans la consigne

- Classe Creature avec tous les attributs demandes
- Classe Personnage qui herite de Creature avec en plus une arme et un inventaire
- Classe Monstre qui herite de Creature avec en plus des resistances
- Le jeu demande combien de heros et de monstres vont combattre
- Selection des personnages et des monstres parmi une liste
- Choix d'une arme pour chaque heros
- Systeme d'attaque avec jet 1d20, reussite critique sur 20 et echec critique sur 1
- Soin sans jet de de avec 2d8
- Buff qui augmente la defense
- Debuff qui reduit la defense de l'ennemi
- Initiative 1d20 pour determiner l'ordre de jeu
- Resistances des monstres qui divisent les degats par 2
- Types de degats : Contondant, Tranchant, Percant, Feu, Poison, Magique
- Gestion des erreurs de saisie
- Cas de victoire et cas de defaite

## Ameliorations

### Amelioration 1 : Empoisonnement et paralysie

Quand une creature avec le type de degats poison touche un heros, ce heros devient empoisonne.
Au tour suivant il perd 5 PV et est paralyse, il ne peut pas jouer ce tour.
L'effet dure un seul tour.

### Resume de fin de combat

A la fin du combat le jeu affiche un resume complet :
- Le nombre de tours qu'a dure le combat
- L'etat de chaque heros (vivant ou mort) avec ses PV restants
- L'etat de chaque monstre (vivant ou vaincu) avec ses PV restants

## Prerequis

Visual Studio Code
