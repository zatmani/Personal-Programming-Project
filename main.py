import os

from time import sleep
import random

def clear_screen():
    os.system('cls' if os.name == "nt" else 'clear')


cards = ['A♡', 'K♡', 'Q♡', 'J♡', 'X♡', '9♡', '8♡', '7♡', '6♡', '5♡', '4♡', '3♡', '2♡', 'A♧', 'K♧', 'Q♧', 'J♧', 'X♧', '9♧', '8♧', '7♧', '6♧', '5♧', '4♧', '3♧', '2♧', 'A♢', 'K♢', 'Q♢', 'J♢', 'X♢', '9♢', '8♢', '7♢', '6♢', '5♢', '4♢', '3♢', '2♢', 'A♤', 'K♤', 'Q♤', 'J♤', 'X♤', '9♤', '8♤', '7♤', '6♤', '5♤', '4♤', '3♤', '2♤',]
print("♣️Welcome to Poker!♣️")
print("I will be your dealer")
num_players = int(input("How many users will be playing?\n"))
while num_players < 2 or num_players > 4:
    print("There must be 2 players minimum and 4 maximum")
    num_players = int(input("How many users will be playing?\n"))
print(f"Ok... Preparing game for {num_players} players")
print("Shuffling cards...")
player_1_m = 500
player_2_m = 500
players_cards = []
player_1_c = random.sample(cards, 2)
players_cards += [player_1_c]
player_2_c = random.sample(cards, 2)
players_cards += [player_2_c]
print(f"Player 1 has {player_1_m}$")
print(f"Player 2 has {player_2_m}$")
cards.remove(player_1_c[0])
cards.remove(player_1_c[1])
cards.remove(player_2_c[0])
cards.remove(player_2_c[1])

if num_players == 3:
    player_3_m = 500
    player_3_c = random.sample(cards, 2)
    players_cards += [player_3_c]
    print(f"Player 3 has {player_3_m}$")
    cards.remove(player_3_c[0])
    cards.remove(player_3_c[1])
if num_players == 4:
    player_3_m = 500
    player_4_m = 500
    print(f"Player 3 has {player_3_m}$")
    print(f"Player 4 has {player_4_m}$")
    player_3_c = random.sample(cards, 2)
    player_4_c = random.sample(cards, 2)
    players_cards += [player_3_c]
    players_cards += [player_4_c]
    cards.remove(player_3_c[0])
    cards.remove(player_3_c[1])
    cards.remove(player_4_c[0])
    cards.remove(player_4_c[1])
num = 1
card = 0
print("Ok, I will show each player their cards starting with player 1.")
input("Enter something when you are ready to see your cards.\n")
for i in range(num_players):
    print(f"Player {num}, I will show you your cards now")
    print("Other players look away now")
    for i in range(5, -1, -1):
        print(i)
        sleep(1)
    print(players_cards[card])
    yes_no = input("Enter something when you have memorized your cards.\n")
    clear_screen()
    num +=1
    card += 1
print("Now we can start playing!")
community_cards = []
community_cards = random.sample(cards, 3)
cards.remove(community_cards[0])
cards.remove(community_cards[1])
cards.remove(community_cards[2])
print("Here are your first 3 cards.")
print(community_cards)
num = 1
bet = 0
pot = 0
minimum_bet = 0
def menu():
    menu = input(f"Player {num} what would you like to do?:\n1. Place a bet\n2. Look at your cards\n3. Tip the dealer😊\n4. Fold\n")

    if menu == "1":
        bet = int(input("Enter an amount to bet"))
        while bet < minimum_bet:
            print("That' not enough money!")
            bet = int(input("Enter an amount to bet"))
        minimum_bet = bet
        pot += bet
    if menu == "2":
        show = num - 1
        print(players_cards[show])
