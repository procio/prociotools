#####################################################################################################################################

def copyList(List):
    newList = list()
    for elem in List:
        if type(elem) is list:
            newList.append(copyList(elem))
        else:
            newList.append(elem)
    return newList

#####################################################################################################################################

def clearList(List):
    for index in range(len(List)):
        List.pop(0)

#####################################################################################################################################

def setter(List):
	List = list(set(List))
	return List
	
#####################################################################################################################################

def join(Iterable, Sep=", "):
	return Sep.join(Iterable)
	
#####################################################################################################################################

def str2lst(Elem):
	if type(Elem) is str: Elem = [Elem]
	else: print "WARNING: expected List or Str"
	return Elem
	
#####################################################################################################################################

def addQuotes(String):
	return "\'"+String+"\'"
	
#####################################################################################################################################

def quotize(Elem):
	if type(Elem) is str:
		return addQuotes(Elem)
	if type(Elem) is list:
		for elem in Elem:
			Elem[Elem.index(elem)] = quotize(elem)
	return Elem	
	
#####################################################################################################################################

def listElem2str(List):
	for elem in List:
		List[List.index(elem)] = str(elem)
	return List
	
#####################################################################################################################################

def are(n, objType):
	List = []
	for time in range(n):
		List.append(objType())
	return tuple(List)
	
#####################################################################################################################################

def importer(callerModuleFileName):					#(__file__) / imports all the modules in its callerModule same dir
	import os
	try:
		nameList = os.listdir(os.path.dirname(callerModuleFileName))	#list of files in the same dir
	except:
		nameList = os.listdir(os.curdir)			#in case you pointed the bash in the same dir (dirname is '')
	nameList.remove(os.path.basename(callerModuleFileName))		#removes itself
	moduleList = []
	for name in nameList:
		name = name.split(".")
		for elem in ["py","pyc"]:
			try: 
				name.remove(elem)			#removes ".py",".pyc" / every name is a list
			except:
				pass	
		module = __import__(name[0])				#imports modules
		moduleList.append(module)				#list of modules dynamically imported
	moduleList = list(set(moduleList))				#removes dupes
	return moduleList						
		
#####################################################################################################################################
		
class dd(dict):	#double dictionary #to be completed, not all functions have been implemented
	def __init__(self, dict0=None):
		self.reg = {}
		self.rev = rd()
		if dict0: self.populate(dict0)
		
	def populate(self, dict0):
		for elem in dict0: self[elem] = dict0[elem]
		
	def __cmp__(self, dict0):
		return self.reg.__cmp__(dict0)
		
	def __contains__(self, key):
		return self.reg.__contains__(key)
		
	def __delitem__(self, key):
		val = self.reg[key]
		self.rev[val].remove(key)
		if not self.rev[val]: del self.rev[val]
		del self.reg[key]
		
	def __eq__(self, dict0):
		return self.reg.__eq__(dict0)
		
	def __ge__(self, dict0):
		return self.reg.__ge__(dict0)
		
	def __gt__(self, dict0):
		return self.reg.__gt__(dict0)
		
	def __iter__(self):
		return self.reg.__iter__()
		
	def __le__(self, dict0):
		return self.reg.__le__(dict0)
	
	def __lt__(self, dict0):
		return self.reg.__lt__(dict0)
		
	def __len__(self):
		return self.reg.__len__()
		
	def __ne__(self, dict0):
		return self.reg.__ne__(dict0)
		
	def __repr__(self):
		return self.reg.__repr__()
		
	def __sizeof__(self):
		return self.reg.__sizeof__()
		
	def __setitem__(self, key, val):
		if self.reg.has_key(key):		#whether a value it's being updated
			del self.rev[self.reg[key]]	#the relevant inverse element in the reversed dict should be deleted
		self.reg[key] = val
		
		self.rev[val] = key
		
	def __getitem__(self, key):
		return self.reg[key]
		
	def clear(self):
		self.reg.clear()
		self.rev.clear()
		
	def has_key(self, key):
		return self.reg.has_key(key)
		
	def items(self):
		return self.reg.items()
		
	def iteritems(self):
		return self.reg.iteritems()
		
	def iterkeys(self):
		return self.reg.iterkeys()
		
	def itervalues(self):
		return self.reg.itervalues()
		
	def keys(self):
		return self.reg.keys()	
		
	def values(self):
		return self.reg.values()	
		
#####################################################################################################################################

class rd(dict): #reversed dictionary
	def __init__(self):
		self.reg = {}
		
	def __cmp__(self, dict0):
		return self.reg.__cmp__(dict0)
		
	def __contains__(self, key):
		return self.reg.__contains__(key)
		
	def __delitem__(self, key):
		del self.reg[key]
		
	def __eq__(self, dict0):
		return self.reg.__eq__(dict0)
		
	def __ge__(self, dict0):
		return self.reg.__ge__(dict0)
		
	def __gt__(self, dict0):
		return self.reg.__gt__(dict0)
		
	def __iter__(self):
		return self.reg.__iter__()
		
	def __le__(self, dict0):
		return self.reg.__le__(dict0)
	
	def __lt__(self, dict0):
		return self.reg.__lt__(dict0)
		
	def __len__(self):
		return self.reg.__len__()
		
	def __ne__(self, dict0):
		return self.reg.__ne__(dict0)
		
	def __repr__(self):
		return self.reg.__repr__()
		
	def __sizeof__(self):
		return self.reg.__sizeof__()
		
	def __setitem__(self, key, val):
		if self.reg.has_key(key): self.reg[key].append(val)
		else: self.reg[key] = [val]
		
	def __getitem__(self, key):
		return self.reg[key]
		
	def clear(self):
		self.reg.clear()
		
	def has_key(self, key):
		return self.reg.has_key(key)
		
	def items(self):
		return self.reg.items()
		
	def iteritems(self):
		return self.reg.iteritems()
		
	def iterkeys(self):
		return self.reg.iterkeys()
		
	def itervalues(self):
		return self.reg.itervalues()
		
	def keys(self):
		return self.reg.keys()	
		
	def values(self):
		List = []
		for value in self.reg.values():
			List += value
		return List	
		
def prova():
	d = dd(dict(a=1,b=2,c=3,d=1))
	return d
		
		

		

