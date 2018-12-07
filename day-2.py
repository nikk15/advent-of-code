import itertools
from difflib import SequenceMatcher

file = open("day-2-input.txt", "r") 
ids = []
for line in file: 
	ids.append(line)

# PART 1

def id_checksum(ids):
	two_count = 0
	three_count = 0
	for code in ids:
		code_two_count = 0
		code_three_count = 0
		for letter in code:
			if code.count(letter) == 2:
				code_two_count += 1
			elif code.count(letter) == 3:
				code_three_count += 1
		if code_two_count > 0:
			two_count += 1
		if code_three_count > 0:
			three_count += 1
	result = two_count*three_count
	return result

# PART 2

file = open("day-2-input.txt", "r") 
ids = []
for line in file: 
	ids.append(line)

def common_ids(ids):
	id_a = ""
	id_b = ""
	for a, b in itertools.combinations(ids, 2):
		s = SequenceMatcher(None, a, b)
		if s.ratio() >= 25/26:
			id_a, id_b = a, b
	letters = "".join([l for l in id_a if l in id_b])
	print(letters)

print(id_checksum(ids))
common_ids(ids)	
