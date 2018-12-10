
file = open("day-5-input.txt", "r") 
polymer = file.read().replace('\n', '')

# PART 1

def polymer_post_reactions(polymer):
	checked = []
	for unit in polymer:
		if checked and unit != checked[-1] and unit.upper() == checked[-1].upper():
			checked.pop(-1)
		else:
			checked.append(unit)
	return len(checked)

# PART 2

def optimal_polymer(polymer):
	minus_units = {}
	for char in "abcdefghijklmnopqrstuvwxyz":
		new_polymer = polymer.replace(char, '')
		new_polymer = new_polymer.replace(char.upper(), '')
		minus_units[char] = polymer_post_reactions(new_polymer)
	return min(minus_units.values())
	

print(polymer_post_reactions(polymer))
print(optimal_polymer(polymer))

