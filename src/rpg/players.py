class Players:
    def __init__(self, *args):
        self.__players = []
        for player in args:
            self.append(player)

    def append(self, player):
        if len(self.__players) >= 2:
            self.__players = self.__players[-1:]
        self.__players.append(player)

    def __getitem__(self, item):
        return self.__players[item]

    def __len__(self):
        return len(self.__players)

    def order(self):
        rolls = dict()
        while len(rolls) < len(self):
            if len(rolls):
                print("Reroll")
            rolls = {p.roll(): p for p in self.__players}
        order = sorted(rolls, reverse=True)
        return (rolls[r] for r in order)
