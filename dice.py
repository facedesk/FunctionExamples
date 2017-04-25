from random import randrange

dice1= randrange(1,7)
dice2 = randrange(1,7)

dice = [randrange(1,4),randrange(1,12)]

d4
d6
d8
d12
d18
d20


print(sum(dice))


def roll():
	result = randrange(1, 7)
	return result

def round(players):
	winscore = 0
	winplayer = ""
	for player in players:
		rolled = roll()
        if(rolled==winscore):
            return ""
        if(rolled > winscore):
        	winscore = rolled
        	winplayer=player[0]
	return winplayer
def game():
    addingPlayers = True
    players = {}
    while(addingPlayers):
    	player =raw_input('''Enter players name. 
Type quit to stop adding
    		''')
    	if(player.lower() == "quit"):
    		addingPlayers = False
        else:
    	    players[player] = 0
    	print players

	gameon= True
    while(gameon):
        winner = round(players)
        if(winner != ""):
            players[winner]= players[winner] + 1
            if(players[winner] == 3):
        	    gameon= False




if __name__ == '__main__':
	game()



