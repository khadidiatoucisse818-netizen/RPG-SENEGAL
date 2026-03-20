import random


def lancer_de(faces):
    return random.randint(1, faces)


def afficher_barre_vie(pv_actuel, pv_max, longueur=20):
    pourcentage = pv_actuel / pv_max
    rempli = int(pourcentage * longueur)
    vide = longueur - rempli
    barre = '#' * rempli + '-' * vide
    return "[" + barre + "] " + str(pv_actuel) + "/" + str(pv_max)


def afficher_titre(texte):
    largeur = 55
    print("=" * largeur)
    print(texte.center(largeur))
    print("=" * largeur)
    print("")


def afficher_menu(titre, options):
    print("\n" + titre)
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])


def saisir_choix(nombre_options):
    while True:
        try:
            choix = int(input("Votre choix : "))
            if 1 <= choix <= nombre_options:
                return choix
            else:
                print("Entrez un nombre entre 1 et " + str(nombre_options))
        except ValueError:
            print("Entree invalide. Entrez un nombre.")
