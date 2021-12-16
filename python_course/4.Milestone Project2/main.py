from deck import Deck
from player import Player

player_one = Player('Player 1')
player_two = Player('Player 2')

new_deck = Deck()
new_deck.shuffle_deck()

#Dealing cards to players one by one
for i in range(len(new_deck.all_cards)):
    player_card = new_deck.deal_one()
    if i % 2 == 0:
        player_one.add_cards(player_card)
    else:
        player_two.add_cards(player_card)

game_on = True
round_number = 0

while game_on:
    round_number += 1
    print(f'Round {round_number} ')

    #Check if game is still playable
    if len(player_one.all_cards) == 0:
        print("Player 2 Won!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player 1 Won!")
        game_on = False
        break

    #Draw card for each player
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print("Player 1 unable to declare war. Player 2 Wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player 2 unable to declare war. Player 1 Wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())

