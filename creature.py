class Creature:

    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.pv_max = pv
        self.defense = defense
        self.type_degats = type_degats
        self.initiative = 0
        self.etats = []
        self.actions = ["Attaquer", "Soigner", "Buff (se renforcer)", "Debuff (affaiblir ennemi)"]

    def est_vivant(self):
        return self.pv > 0

    def afficher_actions(self):
        print("Actions disponibles pour " + self.nom + " :")
        for i in range(len(self.actions)):
            print("  " + str(i + 1) + ". " + self.actions[i])

    def afficher_caracteristiques(self):
        print("Nom : " + self.nom)
        print("Description : " + self.description)
        print("PV : " + str(self.pv) + "/" + str(self.pv_max))
        print("Defense : " + str(self.defense))
        print("Type de degats : " + self.type_degats)
