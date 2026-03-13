print("♣️Welcome to Poker!♣️")
print("I will be your dealer")
num_players = int(input("How many users will be playing?"))
while num_players < 2 or num_players > 4:
    print("There must be 2 players minimum and 4 maximum")
print(f"Ok... Preparing game for {num_players} players")
print("Shuffling cards...")
if num_players == 2:
    player_1 = 500
    player_2 = 500
if num_players == 3:
    player_1 = 500
    player_2 = 500
    player_3 = 500
if num_players == 4:
    player_1 = 500
    player_2 = 500
    player_3 = 500
    player_4 = 500