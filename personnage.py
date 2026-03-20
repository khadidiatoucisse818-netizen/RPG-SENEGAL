import random
from creature import Creature
from arme import sabre, arc_casamance, lance_mystique, epee_empire, massue


class Personnage(Creature):

    def __init__(self, nom, description, pv, defense, type_degats, arme):
        super().__init__(nom, description, pv, defense, type_degats)
        self.arme = arme
        self.inventaire = []

    def equiper_arme(self, arme):
        self.arme = arme
        print(self.nom + " s'equipe de : " + self.arme.nom)

    def soigner_cible(self, cible):
        soin = random.randint(1, 8) + random.randint(1, 8)
        cible.pv = min(cible.pv + soin, cible.pv_max)
        print(self.nom + " soigne " + cible.nom + " de " + str(soin) + " PV.")
        print("PV de " + cible.nom + " : " + str(cible.pv) + "/" + str(cible.pv_max))

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        print("Arme : " + self.arme.nom)
        print("Inventaire : " + str(self.inventaire))


# PV baissés, chaque roi a sa propre arme

lat_dior = Personnage(
    nom="Lat Dior",
    description="Guerrier du Cayor, attaquant redoutable au combat rapproche.",
    pv=40,
    defense=14,
    type_degats="tranchant",
    arme=sabre
)

aline_sitoe = Personnage(
    nom="Aline Sitoe Diatta",
    description="Pretresse resistante de Casamance, maitresse des soins.",
    pv=35,
    defense=13,
    type_degats="magique",
    arme=arc_casamance
)

maba_diakhou = Personnage(
    nom="Maba Diakhou Ba",
    description="Chef religieux du Rip, renforce ses allies.",
    pv=38,
    defense=15,
    type_degats="magique",
    arme=lance_mystique
)

omar_tall = Personnage(
    nom="Omar Foutiyou Tall",
    description="Leader spirituel et militaire, puissant en magie.",
    pv=38,
    defense=13,
    type_degats="magique",
    arme=epee_empire
)

samory_toure = Personnage(
    nom="Samory Toure",
    description="Grand stratege guerrier, inflige beaucoup de degats.",
    pv=42,
    defense=12,
    type_degats="tranchant",
    arme=massue
)

personnages = [lat_dior, aline_sitoe, maba_diakhou, omar_tall, samory_toure]
