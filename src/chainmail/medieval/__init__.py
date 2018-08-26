from rpg.players import Players

from .turn_sequence.move_counter_move import MoveCounterMove
from .turn_sequence.simultaneous import SimultaineousMove


class Battle:
    move_system = MoveCounterMove()

    def __init__(self, *players):
        self.players = Players(*players)
        self.__turns = 5

    def start(self):
        self.__turns = 5
        self.move_system.start(self.players)
        print("Battle stated")

    def finish(self):
        print("Battle finished")

    @property
    def is_finished(self):
        return self.__turns <= 0

    def turn(self):
        print("Next turn")
        self.move_system.turn()
        self.__turns -= 1

    def process(self):
        self.start()
        while not self.is_finished:
            self.turn()
        self.finish()
