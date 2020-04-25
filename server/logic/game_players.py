from .profession import PROFESSION_LIST
from .action import ACTION_LIST

class GamePlayer:
    def __init__(self, player):

        self.name = player["name"]
        self.profession = PROFESSION_LIST[player["profession"]]

        if self.name != "":
            base_hp = self.profession.base_attributes["base_hp"]
            self.hp = (base_hp, base_hp)
            base_ap = self.profession.base_attributes["base_ap"]
            self.ap = (base_ap, base_ap)
            base_mana = self.profession.base_attributes["base_mana"]
            self.mana = (base_mana, base_mana)

            self.oattack = self.profession.base_attributes["offset_attack"]
            self.odefense = self.profession.base_attributes["offset_defense"]
            self.orhp = self.profession.base_attributes["offset_recover_hp"]
            self.ormana = self.profession.base_attributes["offset_recover_mana"]

            self.actions = self.profession.actions

            self.turn_in = 0
        else:
            self.hp = (0,0)
            self.ap = (0,0)
            self.mana = (0,0)
            self.oattack = 0
            self.odefense = 0
            self.orhp = 0
            self.ormana = 0
            self.actions = []
            self.turn_in = 99

    def advance_turn(self, pcount):
        if self.turn_in != 99:
            self.turn_in = self.turn_in % pcount

class GamePlayers:
    def __init__(self, lobby, pcount):
        self.pcount = pcount
        p1 = lobby["p1"]
        self.p1 = GamePlayer(p1)
        p2 = lobby["p2"]
        self.p2 = GamePlayer(p2)
        p3 = lobby["p3"]
        self.p3 = GamePlayer(p3)
        p4 = lobby["p4"]
        self.p4 = GamePlayer(p4)
        p5 = lobby["p5"]
        self.p5 = GamePlayer(p5)
        p6 = lobby["p6"]
        self.p6 = GamePlayer(p6)
