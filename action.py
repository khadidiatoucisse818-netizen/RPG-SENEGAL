import random


class ActionAttaque:

    def __init__(self, lanceur, cible):
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        jet = random.randint(1, 20)
        print(self.lanceur.nom + " attaque " + self.cible.nom + " - jet : " + str(jet))

        if jet == 1:
            degats = self.lanceur.arme.lancer_degats()
            print("Echec critique ! " + self.lanceur.nom + " se blesse de " + str(degats) + " degats !")
            self.lanceur.pv = max(0, self.lanceur.pv - degats)

        elif jet == 20:
            degats = self.lanceur.arme.lancer_degats() * 2
            print("Reussite critique ! Degats doubles : " + str(degats))
            self.cible.pv = max(0, self.cible.pv - degats)
            self.appliquer_poison()

        elif jet >= self.cible.defense:
            degats = self.lanceur.arme.lancer_degats()
            degats = self.verifier_resistance(degats)
            print("Attaque reussie ! " + str(degats) + " degats infliges.")
            self.cible.pv = max(0, self.cible.pv - degats)
            self.appliquer_poison()

        else:
            print("Attaque ratee.")

        print("PV de " + self.cible.nom + " : " + str(self.cible.pv) + "/" + str(self.cible.pv_max))

    def verifier_resistance(self, degats):
        if hasattr(self.cible, 'resistances'):
            if self.lanceur.arme.type_degats in self.cible.resistances:
                degats = degats // 2
                print(self.cible.nom + " resiste ! Degats reduits a " + str(degats))
        return degats

    def appliquer_poison(self):
        # Le poison vient du type_degats de la creature, pas seulement de Mami Wata
        from personnage import Personnage
        if self.lanceur.type_degats == "poison" and isinstance(self.cible, Personnage):
            if "empoisonne" not in self.cible.etats:
                self.cible.etats.append("empoisonne")
                print(self.cible.nom + " est empoisonne par " + self.lanceur.nom + " ! Il perdra 5 PV et sera paralyse au prochain tour.")


class ActionSoin:

    def __init__(self, lanceur, cible):
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        soin = random.randint(1, 8) + random.randint(1, 8)
        self.cible.pv = min(self.cible.pv + soin, self.cible.pv_max)
        print(self.lanceur.nom + " soigne " + self.cible.nom + " de " + str(soin) + " PV.")
        print("PV de " + self.cible.nom + " : " + str(self.cible.pv) + "/" + str(self.cible.pv_max))


class ActionBuff:

    def __init__(self, lanceur, cible):
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        bonus = random.randint(1, 4)
        self.cible.defense += bonus
        print(self.lanceur.nom + " se renforce ! +" + str(bonus) + " en defense.")
        print("Defense de " + self.cible.nom + " : " + str(self.cible.defense))


class ActionDebuff:

    def __init__(self, lanceur, cible):
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        malus = random.randint(1, 4)
        self.cible.defense = max(0, self.cible.defense - malus)
        print(self.lanceur.nom + " affaiblit " + self.cible.nom + " ! -" + str(malus) + " en defense.")
        print("Defense de " + self.cible.nom + " : " + str(self.cible.defense))


def gerer_poison(heros):
    if "empoisonne" in heros.etats:
        heros.pv = max(0, heros.pv - 5)
        print(heros.nom + " subit le poison et perd 5 PV.")
        print(heros.nom + " est paralyse et passe son tour !")
        print("PV restants : " + str(heros.pv) + "/" + str(heros.pv_max))
        heros.etats.remove("empoisonne")
        return True
    return False
