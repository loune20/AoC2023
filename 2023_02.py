import re
games = []
with open('input.txt') as file:
	for line in file:
		games.append([game.strip() for game in line.split(":")[-1].split(";")])

def count_cubes(draw):
	cubes = {"green":0, "blue":0, "red":0}
	for color in cubes.keys():
		if len(res:=re.findall("(\d+)(?: "+color+")", draw)) > 0:
			cubes[color] = int(res[0])
	return(cubes)

# Star 1
ids_pos_games = 0
for game in games:
	game_possible = True
	for draw in game:
		cubes = count_cubes(draw)
		if not((cubes["red"]<= 12) and (cubes["green"]<= 13) and (cubes["blue"]<= 14)):
			game_possible = False
	if game_possible:
		ids_pos_games += games.index(game)+1
print(ids_pos_games)

# Star 2
tot_powers = 0
for game in games:
	max_cubes = {"green":0, "blue":0, "red":0}
	for draw in game:
		cubes = count_cubes(draw)
		if cubes["green"] > max_cubes["green"]: max_cubes["green"] = cubes["green"]
		if cubes["blue"] > max_cubes["blue"]: max_cubes["blue"] = cubes["blue"]
		if cubes["red"] > max_cubes["red"]: max_cubes["red"] = cubes["red"]
	power = max_cubes["green"]*max_cubes["blue"]*max_cubes["red"]
	tot_powers += power
print(tot_powers)