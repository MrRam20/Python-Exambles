import random

class card(object):
	"""constructor for a car"""
	def __init__(self, suit, num):
		super(card, self).__init__()
		self.suit = suit
		self.num = num
	"""returns a string to display"""
	def __str__(self):
		return str(self.suit) + "  " + str(self.num)
	"""calculates the value of the card as a number"""
	def value(self):
		if self.num == "j" or self.num == "q" or self.num == "k":
			return 10
		elif self.num == "a":
			return 1
		else:
			return self.num


class deck(object):
	"""constructor for a deck"""
	def __init__(self):
		super(deck, self).__init__()
		self.pack = []
		suits = ["spade", "diamonds", "hearts", "clubs"]
		values = [2,3,4,5,6,7,8,9,10,"j","q","k","a"]
		for suit in suits:
			for value in values:
				self.pack.append(card(suit, value))
		return

	def shuffle(self):
		random.shuffle(self.pack)

	def hit(self):
		return self.pack.pop()

	def printDeck(self):
		for cardInHand in self.pack:
			print(cardInHand)

def handValue(hand):
	numberOfAces = 0
	totalValue = 0
	for cardInHand in hand:
		value = cardInHand.value()
		if value == 1:
			numberOfAces += 1
		else:
			totalValue += value	

	if numberOfAces == 0:
		return totalValue;
	elif (totalValue + numberOfAces) >= 21:
		return totalValue + numberOfAces
	else:
		"""adds either 1 or 11 for value of an ace"""
		"""if one ace has a value of 11 cause you to have more
		than 21 you only want it to have a value of 1"""
		if totalValue + 10 + numberOfAces >= 21:
			totalValue += numberOfAces
		else:
			"""addes 11 for one ace but 1 for other
			two aces would be a bust of 22"""
			totalValue += 10 + numberOfAces
	return totalValue

while True:
	print("Do you want to play Blackjack?")
	userInput = input()
	if userInput == "y":
		pack = deck()
		pack.shuffle()
		dealer = [pack.hit(), pack.hit()]
		player = [pack.hit(), pack.hit()]
		while True:
			print("Dealer showing  ")
			print(str(dealer[1]))
			print("You have ")
			for playerCard in player:
				print(str(playerCard))
			print("with a value of " + str(handValue(player)))
			print("do you want a hit?  ")
			hitting = input();
			if hitting == "y":
				player.append(pack.hit())
				if handValue(player) > 21:
					print("you loss")
					break
				else:
					pass
			else:
				break
		while handValue(dealer) < handValue(player) or handValue(dealer) < 21:
			dealer.append(pack.hit())
		print("dealers cards ")
		for m in dealer:
			print(str(m))
		print("dealer value " + str(handValue(dealer)))
	else:
		break

