from euler import partitions

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
GOAL = 200
		
goal_combinations = []

print len(partitions(COINS, GOAL))