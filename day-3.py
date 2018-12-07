import collections
import numpy as np

file = open("day-3-input.txt", "r") 

# PREPARATION

def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

claims = []
for line in file: 
	line = line.split()
	line.pop(1)
	line[0] = int(line[0][1:])
	line[1], line[2] = line[1].split(','), line[2].split('x')
	line[1][0], line[1][1] = int(line[1][0]), int(line[1][1][:-1])
	line[2][0], line[2][1] = int(line[2][0]), int(line[2][1])
	line = flatten(line)
	claim = dict(zip(['id', 'x', 'y', 'w', 'h'], line))
	claims.append(claim)

def place_claims(claims):
	fabric_area = np.zeros((1000,1000))
	for claim in claims:
		for i in range(claim['x'], (claim['x'] + claim['w'])):
			for j in range(claim['y'], (claim['y'] + claim['h'])): 
				fabric_area[i,j]+=1
	return fabric_area

# PART 1

def claim_overlaps(claims):
	overlaps = (place_claims(claims) >= 2).sum()
	return overlaps

# PART 2

def no_overlap_id(claims):
	squares = place_claims(claims)
	for claim in claims:
		count = 0
		for i in range(claim['x'], (claim['x'] + claim['w'])):
			for j in range(claim['y'], (claim['y'] + claim['h'])):
				if squares[i, j] == 1:
					count +=1
		if claim['w']*claim['h'] == count:
			return claim['id']
			
print(claim_overlaps(claims))
print(no_overlap_id(claims))






