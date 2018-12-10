from datetime import datetime
from operator import itemgetter

file = open("day-4-input.txt", "r") 

# PREPARATION

schedule = []
for line in file:
	time = {} 
	time['date'] = datetime.strptime(line[1:17],'%Y-%m-%d %H:%M')
	time['details'] = line[19:].strip('\n')
	schedule.append(time)

def sort_schedule(schedule):
	sorted_schedule = sorted(schedule, key=itemgetter('date'))
	return sorted_schedule

# PARTS 1 & 2

def most_asleep(schedule):

	# 1

	schedule = sort_schedule(schedule)
	current_guard = None
	sleep_start = None
	guards = {}
	guard_minutes = {}
	
	for time in schedule:
		if 'begins' in time['details']:
			current_guard = time['details'].split()[1]
		elif 'asleep' in time['details']:
			sleep_start = time['date'].minute
		elif 'wakes' in time['details']:
			guards[current_guard] = guards.get(current_guard, 0) + (time['date'].minute - sleep_start)
			if current_guard not in guard_minutes:
				guard_minutes[current_guard] = {}
			for minute in range(sleep_start, time['date'].minute + 1):
				guard_minutes[current_guard][minute] = guard_minutes[current_guard].get(minute, 0) + 1
	most_minutes_slept = max(guards.values())
	bad_guard_id = [k for k, v in guards.items() if v == most_minutes_slept][0]
	sleepiest_minute = max(guard_minutes[bad_guard_id].values())
	common_minute_slept = [k for k, v in guard_minutes[bad_guard_id].items() if v == sleepiest_minute][0]
	result_part1 = common_minute_slept * int(bad_guard_id[1:])	

	#2
	
	most_slept_minute = None
	max_sleeps_minute = 0
	sleepiest_guard = None

	for guard_id, minute_counts in guard_minutes.items():
		for minute, count in minute_counts.items():
			if count > max_sleeps_minute:
				most_slept_minute = minute
				sleepiest_guard = guard_id
				max_sleeps_minute = count

	result_part2 = most_slept_minute * int(sleepiest_guard[1:])

	return result_part1, result_part2

print(most_asleep(schedule))
