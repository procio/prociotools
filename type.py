import os

def stroke(k, press=False, release=False):
	keys = {"a" : "38",
		"b" : "56",
		"c" : "54",
		"d" : "40",
		"e" : "26",
		"f" : "41",
		"g" : "42",
		"h" : "43",
		"i" : "31",
		"j" : "44",
		"k" : "45",
		"l" : "46",
		"m" : "58",
		"n" : "57",
		"o" : "32",
		"p" : "33",
		"q" : "24",
		"r" : "27",
		"s" : "39",
		"t" : "28",
		"u" : "30",
		"v" : "55",
		"w" : "25",
		"x" : "53",
		"y" : "29",
		"z" : "52",
		"\n" : "36",
		"ALT" : "64",
		"TAB" : "23"
		}
		
	if not press and not release:
		press = release = True
	if press:
		os.system("xsendkeycode %s 1" % keys[k])
	if release:
		os.system("xsendkeycode %s 0" % keys[k])
		
def altTab(hits=1):
	stroke("ALT",press=True)
	for hit in range(hits):
		stroke("TAB")
	stroke("ALT",release=True)
	
def cls():
	os.system("clear")
	

