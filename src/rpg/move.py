class MoveSystem:
    def __init__(self):
        self.movers = None

    def start(self, movers):
        self.movers = movers

    def turn(self):
        raise NotImplementedError("Turn is not implemented")