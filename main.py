from os import system
from time import sleep
import random









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
player_1_c = random.sample(cards, 2) 
player_2_c = random.sample(cards, 2) 
print(f"Player 1 has {player_1_m}$")
print(f"Player 2 has {player_2_m}$")
players_cards = []
players_cards += [player_1_c, player_2_c]
if num_players == 3:
    player_3_m = 500
    print(f"Player 3 has {player_3_m}$")
    player_3_c = random.choice(cards, 2)
if num_players == 4:
    player_3_m = 500
    player_4_m = 500
    print(f"Player 3 has {player_3_m}$")
    print(f"Player 4 has {player_4_m}$")
    player_3_c = random.choice(cards, 2)
    player_4_c = random.choice(cards, 2)
num = 1
card = 0
for i in range(num_players):
    print(f"Player {num}, I will show you your cards now")
    print("Other players look away now")
    for i in range(5, -1, -1):
        print(i)
        sleep(1)
        print(players_cards[card])
    system("cls")
    num +=1
