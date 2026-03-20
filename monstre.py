from creature import Creature
from arme import griffe, queue, morsure, souffle, tentacule, nageoire


class Monstre(Creature):

    def __init__(self, nom, description, pv, defense, type_degats, arme, resistances):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.resistances = resistances

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        print("Arme : " + self.arme.nom)
        print("Resistances : " + str(self.resistances))


# PV baissés, chaque monstre a sa propre arme

mami_wata = Monstre(
    nom="Mami Wata",
    description="Esprit puissant de l'eau, seule detentrice du poison.",
    pv=50,
    defense=20,
    type_degats="poison",
    arme=griffe,
    resistances=["magique"]
)

esprit_fleuve = Monstre(
    nom="Esprit du Fleuve Senegal",
    description="Esprit ancien protecteur des eaux.",
    pv=45,
    defense=18,
    type_degats="contondant",
    arme=queue,
    resistances=["tranchant"]
)

serpent_eau = Monstre(
    nom="Serpent d'eau",
    description="Creature venimeuse du fleuve.",
    pv=30,
    defense=10,
    type_degats="percant",
    arme=morsure,
    resistances=["percant"]
)

djinn_mer = Monstre(
    nom="Djinn de la mer",
    description="Esprit magique des profondeurs.",
    pv=35,
    defense=15,
    type_degats="magique",
    arme=souffle,
    resistances=["percant"]
)

ombre_profondeurs = Monstre(
    nom="Ombre des profondeurs",
    description="Creature mysterieuse et silencieuse.",
    pv=40,
    defense=12,
    type_degats="percant",
    arme=tentacule,
    resistances=["magique"]
)

poisson_demoniaque = Monstre(
    nom="Poisson demoniaque",
    description="Monstre marin tres dangereux.",
    pv=28,
    defense=8,
    type_degats="tranchant",
    arme=nageoire,
    resistances=["tranchant"]
)

monstres = [mami_wata, esprit_fleuve, serpent_eau, djinn_mer, ombre_profondeurs, poisson_demoniaque]
