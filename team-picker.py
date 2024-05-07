from random import randrange

players = ["harold", "collins", "javed", "vincent", "mambato", "jay", "jack", "amrik", "tobi", "levi", "demi", "tim" ]
team1 = []
team2 = []
number_players = len(players) / 2
if number_players - int(number_players) != 0:
    print("Non even number of players!")
else:
    for i in range(int(number_players)):
        player_number = randrange(0,len(players))
        team1.append(players[player_number])
        players.remove(players[player_number])
    team2 = players
    print(team1)
    print(team2)
