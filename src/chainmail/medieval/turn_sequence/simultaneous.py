from . import ChainmailMoveSystem


class SimultaineousMove(ChainmailMoveSystem):
    def turn(self):
        # 1.
        actions = [self.get_action(mover) for mover in self.movers]
        # 2.
        for action in actions:
            self.do_move(action)
        # 3.
        self.artillery()
        # 4.
        self.missile()
        # 5.
        self.melee()
