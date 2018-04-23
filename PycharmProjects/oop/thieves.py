import random


from attributes import Agile, sneaky
from character import  Character


class Thief(Agile, sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
