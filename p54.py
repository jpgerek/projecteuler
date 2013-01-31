from itertools import chain
from collections import defaultdict

f = open('poker.txt', 'r')

ONE_PAIR = 200
TWO_PAIRS = 400
THREE_OF_A_KIND = 600
STRAIGHT = 800
FLUSH = 1000
FULL_HOUSE = 1200
FOR_OF_A_KIND = 1400
STRAIGHT_FLUSH = 1600
ROYAL_FLUSH = 1800

CARD_VALUES = { card: value for card, value in chain(((str(x), x) for x in xrange(2, 10)), (('T', 10), ('J', 11), ('Q', 12), ('K', 13), ('A', 14))) }

PLAYER_1 = 1
PLAYER_2 = 2

def poker_hand_value(cards):
	cards.sort()
	
	all_same_suit = len(set(map(lambda (value, suit): suit, cards))) == 1
	
	card_values = map(lambda (value, suit): value, cards)
	
	#- Royal flush -#
	if all_same_suit and [10, 11, 12, 13, 14] == card_values:
		return ('ROYAL_FLUSH', ROYAL_FLUSH)
	
	are_consecutive_values = range(card_values[0], card_values[0]+len(card_values)) == card_values
	
	#- Straight flush -#
	if all_same_suit and are_consecutive_values:
		return ('STRAIGHT_FLUSH', STRAIGHT_FLUSH)

	#- Counting repeated cars -#
	cards_count_dict = defaultdict(int)
	for value in card_values:
		cards_count_dict[value] += 1
	(card1, count1), (card2, count2) = sorted(cards_count_dict.items(), cmp=lambda a, b: b[1] - a[1])[:2]
	
	#- Four of a kind -#
	if count1 == 4:
		return ('FOR_OF_A_KIND', FOR_OF_A_KIND + (card1 * 10) + card2)
	
	#- Full house -#
	if count1 == 3 and count2 == 2:
		return ('FULL_HOUSE', FULL_HOUSE + (card1 * 10) + card2)
	
	#- Flush -#
	if all_same_suit:
		highest_card = max(card_values)
		return ('FLUSH', FLUSH + highest_card)
	
	#- Straight #-
	if are_consecutive_values:
		highest_card = max(card_values)
		return ('STRAIGHT', STRAIGHT + highest_card)
	
	#- Three of a kind -#
	if count1 == 3:
		highest_card = max(filter(lambda value: value != card1, card_values))
		return ('THREE_OF_A_KIND', THREE_OF_A_KIND + (card1 * 10) + highest_card)

	#- Two pairs -#
	if count1 == 2 and count2 == 2:
		highest_card = max(filter(lambda value: value not in (card1, card2), card_values))
		return ('TWO_PAIRS', TWO_PAIRS + (card1 + card2) * 10 + highest_card)
	
	#- One pair -#
	if count1 == 2:
		#- Highest card without counting the pair -#
		highest_card = max(filter(lambda value: value != card1, card_values))
		return ('ONE_PAIR', ONE_PAIR + (card1 * 10) + highest_card)
	
	#- High Card -#
	highest_card = max(card_values)
	return ('HIGHEST_CARD', highest_card)

def get_cards_from_line(line):
	cards = map(lambda card: (card[0], card[1]), line.rstrip('\n').split(' '))
	return list(map(lambda (card, suit): (CARD_VALUES[card], suit), player_cards) for player_cards in (cards[:5], cards[5:]))

def unit_tests():
	tests = (
			("5H 5C 6S 7S KD 2C 3S 8S 8D TD", PLAYER_2, "Pair of fives and pair of eights"),
			("5D 8C 9S JS AC 2C 5C 7D 8S QH", PLAYER_1, "Highest card Aces and highest card Queen"),
			("2D 9C AS AH AC 3D 6D 7D TD QD", PLAYER_2, "Three aces and Flush with Diamonds"),
			("4D 6S 9H QH QC 3D 6D 7H QD QS", PLAYER_1, "Pair of queens highest card Nine and pair of queens highest card Seven"),
			("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D", PLAYER_1, "Full House with three fours and full house with three threes"),
			("7H 7C 7S 7D AD 5H 5C 5S 8D 8D", PLAYER_1, "For sevens highest card Aces and full house"),
			("8C TS KC 9H 4S 7D 2S 5D 3S AC", PLAYER_2, "Highest card ace and highest card king"),
			("5C AD 5D AC 9C 7C 5H 8D TD KS", PLAYER_1, "Two pairs of aces and fives and and highest card King"),
			("2H 3H 4H 5C 6H 3S 5S 6S QH AS", PLAYER_1, "Straight and highest card ace"),
			("TC JC QC KC AC 2C 3C 4C 5C 6C", PLAYER_1, "Royal flush and straight flush"),
			)
	for line, supposed_winner, description in tests:
		print description
		player1_cards, player2_cards = get_cards_from_line(line)
		player1_hand, player1_hand_value = poker_hand_value(player1_cards)
		player2_hand, player2_hand_value = poker_hand_value(player2_cards)
		print "\tplayer1: %s, %d" % (player1_hand, player1_hand_value)
		print "\tplayer2: %s, %d" % (player2_hand, player2_hand_value)
		if player1_hand_value > player2_hand_value:
			hand_winner = PLAYER_1
		else:
			hand_winner = PLAYER_2
		assert supposed_winner == hand_winner

	print "All tests passed!"

result = []

for line in f.xreadlines():
	player1_cards, player2_cards = get_cards_from_line(line) 
	player1_hand, player1_hand_value = poker_hand_value(player1_cards)
	player2_hand, player2_hand_value = poker_hand_value(player2_cards)
	if player1_hand_value > player2_hand_value:
		result.append((player1_hand, player1_hand_value, player2_hand, player2_hand_value))

print len(result)