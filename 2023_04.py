cards = []
with open("input.txt") as file:
	for line in file:
		c = line.split(": ")[1].split("|")
		# cards.append({ #star 1
		# 	"winning":[int(num) for num in c[0].strip().split(" ") if num.strip() != ""],
		# 	"present":[int(num) for num in c[1].strip().split(" ") if num.strip() != ""],
		# 	"score": 0
		# 	})
		cards.append({ #star 2
			"winning":[int(num) for num in c[0].strip().split(" ") if num.strip() != ""],
			"present":[int(num) for num in c[1].strip().split(" ") if num.strip() != ""],
			"copies": 1
			})
# Star 1
for c in cards:
	for num in c["present"]:
		if num in c["winning"]:
			if c["score"] == 0:
				c["score"] = 1
			else:
				c["score"] = c["score"]*2

score = 0
for c in cards:score+=c["score"]
print(score)

# Star 2
for c in range(len(cards)):
	for copies in range(cards[c]["copies"]):
		total_win_numbers = 0
		for num in cards[c]["present"]:
			if num in cards[c]["winning"]:
				total_win_numbers += 1
		for i in range(1, total_win_numbers+1):
			cards[c+i]["copies"] += 1

cards_count = 0
for c in range(len(cards)):
	# print("Card", c+1, "copies", cards[c]['copies'])
	cards_count += cards[c]['copies']
print(cards_count)