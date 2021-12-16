class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        print(f'Created {name}')

    def remove_card(self):
        return self.all_cards.pop(0) #Remove from the top of the list

    def add_cards(self, new_cards):
        #Adding multiple card objects at the bottom of the list
        if (type(new_cards) == type([])):
            self.all_cards.extend(new_cards)
        #Adding single card object at the bottom of the list
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# new_player = Player('Jose')

# print(new_player)