import random


class Arme:

    def __init__(self, nom, degats, type_degats):
        self.nom = nom
        self.degats = degats
        self.type_degats = type_degats

    def lancer_degats(self):
        parties = self.degats.split('d')
        nb_des = int(parties[0])
        faces = int(parties[1])
        total = 0
        for i in range(nb_des):
            total += random.randint(1, faces)
        return total


# Armes des rois - noms generiques et types varies
sabre          = Arme("Sabre Royal",       "5d10", "tranchant")
arc_casamance  = Arme("Arc de Guerre",     "3d12", "percant")
lance_mystique = Arme("Lance Sacree",      "4d8",  "feu")
epee_empire    = Arme("Epee Imperiale",    "6d8",  "magique")
massue         = Arme("Massue de Guerre",  "7d6",  "contondant")

# Armes des monstres
griffe         = Arme("Griffes Mortelles",   "4d8",  "poison")
queue          = Arme("Queue Devastatrice",  "6d6",  "contondant")
morsure        = Arme("Morsure Sauvage",     "3d10", "percant")
souffle        = Arme("Souffle Magique",     "5d6",  "feu")
tentacule      = Arme("Tentacule Sombre",    "4d10", "tranchant")
nageoire       = Arme("Nageoire Coupante",   "3d8",  "tranchant")

armes = [sabre, arc_casamance, lance_mystique, epee_empire, massue]
