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
