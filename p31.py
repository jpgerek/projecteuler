
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
GOAL = 200
		
goal_combinations = []

#- From stackoverflow http://stackoverflow.com/a/7825718/311928 -#
def partition(coins, goal):
	if goal == 0 or not coins:
		return []
	this_goal = coins[0]
	remaining_coins = coins[1:]
	results = []
	for qty in xrange(1 + (goal / this_goal)):
		remaining_goal = goal - (qty * this_goal)
		if remaining_goal == 0:
			results.append([qty] + [0] * len(remaining_coins))
		else:
			for option in partition(remaining_coins, remaining_goal):
				results.append([qty] + option)
	return results

print len(partition(COINS, GOAL))