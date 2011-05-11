from prociotools.cards import seed, card, deck

backs = ["blue","red","green","yellow","orange","cyan","white","black"]
decks = {	"piacentine"	:	[[10], ["Coppe","Denari","Bastoni","Spade"], ["Green","Yellow","Gray","Blue"]]	,
		"french"	:	[[13], ["Hearts","Diamonds","Clubs","Spades"], ["Red","Purple","Green","Blue"]]
	 }	#better structure needed.

class commonDeck(deck):
	def __init__(self, name, back=0):
		self.name = name
		self.c = decks[self.name][0][0]
		self.s = self.generateSeeds()
		self.b = backs[back]
		
	def generateSeeds(self):
		seedList = []
		for seedName in decks[self.name][1]: 
			s = seed(seedName, decks[self.name][2][decks[self.name][1].index(seedName)])
			seedList.append(s)
		return seedList
		
	def reds(self):
		reds 	= self.s[0:(len(self.s)/2)]
		#blacks	= self.s[(len(self.s)/2):(len(self.s))]
		return reds
		
class multiDeck(deck):
	def __init__(self, how_many_decks, name):
		cd = None
		for elem in range(how_many_decks):
			cd = commonDeck(name, back=elem)
			cd.generateCards(reds=cd.reds())
			self += cd
		self.c = cd.c
		self.s = cd.s
		self.b = "multi"
		self.t = self.c*len(self.s)*how_many_decks
	
class piacentine(deck):
	def __init__(self):
		cd = commonDeck("piacentine")
		self.c = cd.c
		self.s = cd.s
		self.b = cd.b
		self.generateCards(reds=cd.reds())
		
class french(deck):
	def __init__(self):
		cd = commonDeck("french")
		self.c = cd.c
		self.s = cd.s
		self.b = cd.b
		self.generateCards(reds=cd.reds())
		
		
		

