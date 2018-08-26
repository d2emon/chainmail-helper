import logging

from rpg.pc import PlayerCharacter
from rpg.dice import roll


class Player(PlayerCharacter):
    def roll(self):
        res = roll()
        logging.debug("%s rolls a die (%d)", self.name, res)
        return res
