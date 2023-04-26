class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a, b):
        # compare first score
        # then name
        # if a < b then -1
        # if a == b then 0
        # if a > b then 1
        if a.score != b.score:
            return b.score - a.score
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0


# create a list of Player objects
players = [Player("amy", 100), Player("david", 100), Player("heraldo", 50), Player("aakansha", 75),
           Player("aleksa", 150)]

# sort the list using the comparator function
sorted_players = sorted(players, key=Player.comparator)

# print the sorted list
for player in sorted_players:
    print(player)
