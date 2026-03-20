import random
from utils import lancer_de, afficher_barre_vie, afficher_titre, afficher_menu, saisir_choix
from action import ActionAttaque, ActionSoin, ActionBuff, ActionDebuff, gerer_poison
from arme import sabre, arc_casamance, lance_mystique, epee_empire, massue, armes
from personnage import personnages
from monstre import monstres


def selectionner_personnages():
    afficher_titre("SELECTION DES HEROS")

    # Demander combien de personnages vont combattre
    print("Combien de heros vont combattre ? (1 a " + str(len(personnages)) + ")")
    nb = saisir_choix(len(personnages))

    equipe = []
    disponibles = list(personnages)

    for i in range(nb):
        options = [p.nom for p in disponibles]
        afficher_menu("Choisissez un heros :", options)
        index = saisir_choix(len(options)) - 1
        heros = disponibles.pop(index)

        # Choisir une arme pour chaque heros
        options_armes = [a.nom for a in armes]
        afficher_menu("Choisissez une arme pour " + heros.nom + " :", options_armes)
        index_arme = saisir_choix(len(armes)) - 1
        heros.equiper_arme(armes[index_arme])

        equipe.append(heros)

    return equipe


def selectionner_monstres():
    afficher_titre("SELECTION DES MONSTRES")

    # Demander combien de monstres vont combattre
    print("Combien de monstres vont combattre ? (1 a " + str(len(monstres)) + ")")
    nb = saisir_choix(len(monstres))

    equipe_monstres = []
    disponibles = list(monstres)

    for i in range(nb):
        options = [m.nom for m in disponibles]
        afficher_menu("Choisissez un monstre :", options)
        index = saisir_choix(len(options)) - 1
        monstre = disponibles.pop(index)
        equipe_monstres.append(monstre)

    return equipe_monstres


def lancer_initiatives(combattants):
    print("\nLancer d'initiative :")
    for c in combattants:
        c.initiative = lancer_de(20)
        print(c.nom + " : " + str(c.initiative))
    combattants.sort(key=lambda x: x.initiative, reverse=True)
    print("\nOrdre de jeu :")
    for c in combattants:
        print("  " + c.nom)
    return combattants


def afficher_etat_combat(equipe, ennemis):
    print("\n--- Etat du combat ---")
    for h in equipe:
        statut = " (EMPOISONNE)" if "empoisonne" in h.etats else ""
        print(h.nom + statut + " : " + afficher_barre_vie(h.pv, h.pv_max))
    for m in ennemis:
        print(m.nom + " : " + afficher_barre_vie(m.pv, m.pv_max))


def jouer_tour(creature, allies, ennemis):
    print("\n--- Tour de " + creature.nom + " ---")

    paralyse = gerer_poison(creature)
    if paralyse:
        return

    creature.afficher_actions()
    choix = saisir_choix(4)

    if choix == 1:
        vivants = [e for e in ennemis if e.est_vivant()]
        if len(vivants) > 0:
            afficher_menu("Choisissez une cible :", [e.nom for e in vivants])
            cible = vivants[saisir_choix(len(vivants)) - 1]
            ActionAttaque(creature, cible).executer()

    elif choix == 2:
        vivants = [a for a in allies if a.est_vivant()]
        afficher_menu("Choisissez un allie a soigner :", [a.nom for a in vivants])
        cible = vivants[saisir_choix(len(vivants)) - 1]
        ActionSoin(creature, cible).executer()

    elif choix == 3:
        ActionBuff(creature, creature).executer()

    elif choix == 4:
        vivants = [e for e in ennemis if e.est_vivant()]
        if len(vivants) > 0:
            afficher_menu("Choisissez une cible a affaiblir :", [e.nom for e in vivants])
            cible = vivants[saisir_choix(len(vivants)) - 1]
            ActionDebuff(creature, cible).executer()


def afficher_resume(equipe, ennemis, nb_tours):
    afficher_titre("FIN DU JEU")
    print("Nombre de tours : " + str(nb_tours))
    print("")
    print("--- Heros ---")
    for h in equipe:
        if h.est_vivant():
            print(h.nom + " : VIVANT - PV restants : " + str(h.pv) + "/" + str(h.pv_max))
        else:
            print(h.nom + " : MORT")
    print("")
    print("--- Monstres ---")
    for m in ennemis:
        if m.est_vivant():
            print(m.nom + " : VIVANT - PV restants : " + str(m.pv) + "/" + str(m.pv_max))
        else:
            print(m.nom + " : VAINCU")


def boucle_combat():
    afficher_titre("ROYAUMES DU SENEGAL - COMBAT RPG")

    equipe = selectionner_personnages()
    ennemis = selectionner_monstres()

    print("")
    print("Vos heros :")
    for h in equipe:
        print("  " + h.nom + " : " + h.description)

    print("")
    print("Vos monstres :")
    for m in ennemis:
        print("  " + m.nom + " : " + m.description)

    tous = equipe + ennemis
    ordre = lancer_initiatives(tous)

    nb_tours = 0
    combat_termine = False

    while not combat_termine:
        nb_tours += 1
        afficher_etat_combat(equipe, ennemis)

        for p in ordre:
            if not p.est_vivant():
                continue

            if p in equipe:
                jouer_tour(p, equipe, ennemis)
            else:
                jouer_tour(p, ennemis, equipe)

            if not any(h.est_vivant() for h in equipe):
                combat_termine = True
                break
            if not any(m.est_vivant() for m in ennemis):
                combat_termine = True
                break

    if any(h.est_vivant() for h in equipe):
        afficher_titre("VICTOIRE ! Les royaumes du Senegal triomphent !")
    else:
        afficher_titre("DEFAITE... Les royaumes sont tombes.")

    afficher_resume(equipe, ennemis, nb_tours)


if __name__ == "__main__":
    boucle_combat()
