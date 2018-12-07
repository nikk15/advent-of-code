file = open("day-1-input.txt", "r") 
frequencies = []
for line in file: 
	frequencies.append(line)

# PART 1

def sum_frequencies(frequencies):
	nums = []
	for num in frequencies:
		if num[0] == "+":
			nums.append(int(num[:-1]))
		else:
			nums.append(int(num))
	return sum(nums)

# PART 2

def repeat_frequencies(frequencies):
	tracked = set()
	current_frequency = 0
	while True:
		for num in frequencies:
			if num[0] == "+":
				current_frequency += int(num[:-1])
				if current_frequency in tracked:
					return current_frequency
				else:
					tracked.add(current_frequency)

			else:
				current_frequency += int(num)
				if current_frequency in tracked:
					return current_frequency
				else:
					tracked.add(current_frequency)

print(sum_frequencies(frequencies))
print(repeat_frequencies(frequencies))
