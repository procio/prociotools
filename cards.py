class seed():
	def __init__(self, name, color=None):
		self.n = name
		self.c = color
		
	def __str__(self):
		return self.n

class card(object):
	def __init__(self, number=None, seed=None, back=None, color=None):				
		self.n = number
		self.s = seed
		self.c = color
		self.b = back
		
	def __str__(self):
		colors = True
		number = self.n
		seed = self.s
		figures = {	11	:	"J",
				12	:	"Q",
				13	:	"K",
				1	:	"A"	}
		if number in figures: number = figures[number]
		if colors: 
			from prociotools.colors import color
			seed = color(seed.n, seed.c)
		return ("%s %s" %(str(number), str(seed)))	#return str(number)+" "+str(seed)

	def __gt__(self, card):
		if self.n > card.n:
			return True
		return False

	def __eq__(self, card):
		if self.n == card.n:
			return True
		return False

	def __ge__(self, card):
		return self.__gt__(card) or self.__eq__(card)

	def __le__(self, card):
		return not self.__gt__(card)

	def __lt__(self, card):
		return not self.__ge__(card)
		
class deck(list):
	def __init__(self, cards=None, seeds=None, back=None):
		self.c = cards
		self.s = seeds
		self.b = back
		if seeds: self.t = cards*len(seeds)#da rifare con logica inserimento carta
		
	def generateCards(self, reds=False):
		try:
			for seed in self.s:
				for number in range(1,self.c+1):
					if reds:
						if seed.n in reds:	color = "red"
						else:			color = "black"
					c = card(number, seed, self.b, color)
					self.append(c)
		except:
			raise ValueError, "DeckError: Deck is plain"
		
	def __str__(self):
		from prociotools.meta import join
		cardList = []
		result = ""
		for card in self: cardList.append(str(card))
		if cardList:	
			result = join(cardList, "\n")
		else:	result = "[Deck is empty]"
		return result
		
class hand(list):
	def __init__(self, max_length, min_length):
		self.max_length = max_length
		self.min_length = min_length

class dealer(object):
	def __init__(self, table):
		self.t=table

	def shuffle(self):
		random.shuffle(self.t.getdeck())

	def locatebutton(self):
		self.shuffle()
		self.deal(1)
		dic={}
		maxcards=[]
		for elem in t.playerlist:
			dic[elem.hand[0]]=elem
		maxcard=max(dic.keys())
		for card in dic.keys():
			if card==maxcard:
				maxcards.append(card)
		rmaxcard=max(maxcards, key=lambda x : x.s)
		buttonplayer=dic[rmaxcard]
		buttonplayer.status.append("dealer")

	def setplayersstatus(self):
		pass

#		buttonplayer=None
#		for elem in ci(self.playerlist):
#			if "dealer" in elem.status:
#				buttonplayer=elem
#				print "ok"

	def deal(self, cards=0):
		deck=self.t.getdeck()
		playerlist=self.t.playerlist
		if cards==0:
			cards=self.t.number_of_cards
		for num_elem in range(cards):
			for player_elem in playerlist:
				player_elem.takecard(deck.pop(0))

	def showdeck(self):
		for elem in self.t.getdeck():
			print elem

	def burn(self):
		return self.t.getdeck().pop(0)

	def dealcc(self, ncards):
		dealtcards=[]
		self.burn()
		for elem in range(ncards):
			dealtcards.append(burn())
		self.t.setcommons(dealtcards)

class table(object):
	def __init__(self, players=6, number_of_cards=2, initial_stack=1500):
		self.players=players
		self.initial_stack=initial_stack

		self.generatedeck()
		self.generateplayers()
		self.sitplayers()

	def generatedeck(self, number_of_decks=1):
		self.deck=[]
		for deck in range(number_of_decks):
			for seed in range(4):
				for number in range(2,15):
					c = card(number, seed)
					self.deck.append(c)

	def getdeck(self):
		return self.deck

	def generateplayers(self):
		self.playerlist=[]
		for elem in range(self.players):
			self.playerlist.append(player(elem+1, self.initial_stack))

	def getplayers(self):
		return self.playerlist

	def sitplayers(self):
		import random
		random.shuffle(self.playerlist)

	def getactiveplayers(self):
		activeplayers=[]
		for elem in self.getplayers():
			activeplayers.append(elem)
		return activeplayers

	def setcommons(self, cards):
		for elem in cards:
			self.commoncards.append(elem)

	def clearcommons(self):
		self.commoncards=[]

	def getflop(self):
		return self.commoncards[0:3]

	def getturn(self):
		return self.commoncards[3:4]

	def getriver(self):
		return self.commoncards[4:5]
		
class player(object):
	def __init__(self, number, initial_stack):
		self.initial_stack=initial_stack
		self.hand=[]
		self.name="Player"+str(number)
		self.status=[]
		self.score=[]
	
	def showcards(self):
		self.info=self.name+": "
		for elem in self.hand:
			self.info+=str(elem)
			if elem!=self.hand[len(self.hand)-1]:
				self.info+=", "
		print self.info

	def takecard(self, card):
		self.hand.append(card)

	def discard(self):
		for elem in self.hand:
			self.hand.pop(0)



