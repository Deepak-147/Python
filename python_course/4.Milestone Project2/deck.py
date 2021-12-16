from card import Card
from global_variables import suits, ranks
import random

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

        print('Created New Deck of cards')

    def shuffle_deck(self):
        print("\nShuffling cards...\n")
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# new_deck = Deck()

# for card_object in new_deck.all_cards:
#     print(card_object)

# new_deck.shuffle_deck()

# for card_object in new_deck.all_cards:
#     print(card_object)

# my_card = new_deck.deal_one()
# print(my_card)