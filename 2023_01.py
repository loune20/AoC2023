import re
data = []
with open("input.txt") as file:
	for line in file:
		data.append(line.strip())

# Star 1
sum_calib = 0
for line in data:
	regres=re.findall("\d", line)
	calib = regres[0] + regres[-1]
	sum_calib += int(calib)
print(sum_calib)


# Star 2
map_num = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
for i in range(1, 10):map_num[str(i)] = i

sum_calib = 0
for line in data:
	regres=re.findall("(?=(\d))|(?=(one))|(?=(two))|(?=(three))|(?=(four))|(?=(five))|(?=(six))|(?=(seven))|(?=(eight))|(?=(nine))", line)
	digits = []
	for i in regres:
		res = [r for r in i if r != '']
		digits.extend(res)
	calib = str(map_num[digits[0]]) + str(map_num[digits[-1]])
	sum_calib += int(calib)
print(sum_calib)