
def getScore(List):
	from pt.meta import are
	cardNumbers, cardSeeds, counts = are(3, dict)
	for elem in List:
		cardNumbers[elem] = elem.getNumber()
		cardSeeds[elem] = elem.getSeed()
	occurrencies = list(set(cardNumbers.values()))	
	for value in occurrencies:
		counts[value] = cardNumbers.values().count(value)
	pass###
	
def determine(List):
	from pt.meta import setter, are
	Dict = {}
	Set = setter(List)
	for n in Set:
		Dict[n] = List.count(n)
	#2k, 3k, 4k = are(3,list)
	for n in Dict:
		if Dict[n] is 2:
			pass###
			
class score(object):
	def check(self, elem):
		if type(elem) is not type(self):
			raise ValueError, "ConfrontationError: cannot confront %s and %s" %(type(self), type(elem))
	
	def __gt__(self):
		pass
		
	def __eq__(self):
		pass	
			
	def __ge__(self, elem):
		return self.__gt__(elem) or self.__eq__(elem)

	def __le__(self, elem):
		return not self.__gt__(elem)

	def __lt__(self, elem):
		return not self.__ge__(elem)
	
class pair(score):
	def __init__(self, value, strenght=1):
		self.v = value
		self.s = strenght
		
	def __gt__(self, elem):
		if self.s > elem.s: return True
		if self.s < elem.s: return False
		
		if self.v > elem.v: return True
		return False

	def __eq__(self, elem):
		if self.s != elem.s: return False 
		
		if self.v == elem.v: return True
		return False
		
	def __str__(self):
		return "Pair of %ds" %self.v
		
class twoPairs(score):
	def __init__(self, pair1, pair2, strenght=2):
		pairs = [pair1, pair2]
		self.pair1 = max(pairs)
		self.pair2 = min(pairs)
		self.s = strenght
		
	def __gt__(self, elem):
		if self.s > elem.s: return True
		if self.s < elem.s: return False
		
		if self.pair1 > elem.pair1: return True
		if self.pair1 < elem.pair1: return False
		if self.pair2 > elem.pair2: return True
		return False

	def __eq__(self, elem):
		if self.s != elem.s: return False
		 
		if self.pair1 != elem.pair1: return False
		if self.pair2 != elem.pair1: return False
		return True
		
	def __str__(self):
		return "Two Pairs: %ds and %ds" %(self.pair1.v, self.pair2.v)
		
class tris(score):
	def __init__(self, value, strenght=3):
		self.v = value
		self.s = strenght
		
	def __gt__(self, elem):
		if self.s > elem.s: return True
		if self.s < elem.s: return False
		
		if self.v > elem.v: return True
		return False

	def __eq__(self, elem):
		if self.s != elem.s: return False
		 
		if self.v != elem.v: return False
		return True
		
	def __str__(self):
		return "3 of a kind: %ds" %self.v
		


