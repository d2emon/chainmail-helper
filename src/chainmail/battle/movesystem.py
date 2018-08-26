from rpg.move import MoveSystem


class ChainmailMoveSystem(MoveSystem):
    def move_figures(self, mover):
        print("{} moves its figures".format(mover.name))

    def artillery(self):
        print("Artillery fire is taken")

    def missile(self):
        print("Missile fire is taken")

    def melee(self):
        print("Melees are resolved")


"""
THE SIMULTANEOUS MOVEMENT SYSTEM
1. Both sides write orders for each of their units (groups of figures of like
2. Both sides move their units according to their written orders, making one-
half of the move, checking for unordered melee contact due to opponent
movement, and conducting split-moves and missile fire and taking any
pass-through fire; then the balance of movement is completed as ordered.
type), including direction of movement and facing.
3. Artillery fire is taken.
4. Missile fire is taken.
5. Melees are resolved.
Note: Exact orders for each unit (group of figures of like type) must be given.
Cavalry may be given the order to "Charge if Charged" (CIC), either in
their own behalf or in support of any nearby friendly unit. Such CIC move-
ment begins at the one-half move and is only half of a normal charge,
i.e., a unit of medium horse CIC to support a unit of archers would move
up to 12" during the second half of the turn.
MORALE CHECKS ARE NOT INDICATED IN EITHER OF THE TWO
OF MOVEMENT AS MORALE CHECKS CAN OCCUR DURING THE
AND/OR MELEE PORTIONS OF ANY GIVEN TURN, DEPENDING
CIRCUMSTANCES. HOWEVER, MORALE CHECKS MUST BE MADE
WHATEVER SEGMENT OF THE TURN THE RULES REQUIRE.
SYSTEMS
"""


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
