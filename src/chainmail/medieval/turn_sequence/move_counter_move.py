from . import ChainmailMoveSystem


class MoveCounterMove(ChainmailMoveSystem):
    def turn(self):
        # 1.
        move, counter_move = self.movers.order()
        # 2.
        self.move_figures(move)
        # 3.
        self.move_figures(counter_move)
        # 4.
        self.artillery()
        # 5.
        self.missile()
        # 6.
        self.melee()