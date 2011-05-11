import datetime

def change(date, days=0, months=0, years=0):
	years += months / 12
	months %= 12
	
	if years:	date = addYears(date, years)
	if months:	date = addMonths(date, months)
	if days:	date = addDays(date, days)
	print date
	return date
		
def addYears(date, years):
	try:
		date = datetime.date(day=date.day,month=date.month,year=date.year+years)
	except:
		date = datetime.date(day=28,month=2,year=date.year+years)
	return date
	
def addMonths(date, months):
	delta = date.month + months
	
	if delta < 1:
		date = addYears(date,-1)
		delta += 12
	
	elif delta > 12:
		date = addYears(date,1)
		delta -= 12
			
	try:
		date = datetime.date(day=date.day,month=delta,year=date.year)##
	except:
		try:
			date = datetime.date(day=date.day-1,month=delta,year=date.year)
		except:
			try:
				date = datetime.date(day=date.day-2,month=delta,year=date.year)
			except:
				date = datetime.date(day=date.day-3,month=delta,year=date.year)	
	return date
		
def addDays(date, days):
	date += datetime.timedelta(days)
	return date
