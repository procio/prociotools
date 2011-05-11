start = "\033["
end = "m"

colorsList = {
"Black"		: "0;30",
"LightBlack"	: "1;30",
"Blue"		: "0;34",
"LightBlue"	: "1;34",
"Green"		: "0;32",
"LightGreen"	: "1;32",
"Cyan"		: "0;36",
"LightCyan"	: "1;36",
"Red"		: "0;31",
"LightRed"	: "1;31",
"Purple"	: "0;35",
"LightPurple"	: "1;35",
"Brown"		: "0;33",
"Yellow"	: "1;33",
"Gray"		: "0;37",
"White"		: "1;37",
"Bold"		: "1",
"Restore"	: "0"		}

def getTag(col):
	return "%s%s%s" %(start, colorsList[col], end)

def color(var, col):				#returns a string ready to be printed colorfully
	return "%s%s%s" %(getTag(col), str(var), getTag("Restore"))

def colors():
	for elem in colorsList:
		print color(elem, elem)
