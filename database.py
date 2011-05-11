from prociotools.meta import *

class ProgrammingError(Exception):
	pass

class database():
	def __init__(self, path):
		import sqlite3
		self.c = sqlite3.Connection(path)
		
	def createTable(self, tableName, tableFields):
		statement = "CREATE TABLE "+tableName+" ("
		for elem in tableFields:
			temp = join(elem," ")
			try:
				temp += " "+elem[2]
			except:
				pass
			tableFields[tableFields.index(elem)] = temp
		statement += join(tableFields)+")"
		self.c.execute(statement)
		
	def deleteTable(self, tableName):
		statement = "DROP TABLE "+tableName
		self.c.execute(statement)
		
	def deleteTables(self, tableNames):
		for table in tableNames:
			self.deleteTable(table)
		
	def commit(self):
		statement = "COMMIT"
		self.c.execute(statement)

	def undoAll(self):
		statement = "ROLLBACK"
		self.c.execute(statement)
	
	def insert(self, tableName, values):
		statement = "INSERT INTO "+tableName
		statement += " VALUES ("+join(values)+")"
		self.c.execute(statement)

	def update(self, tableName, columns, values, wcolumns=False, wvalues=False, logOp="="):
		statement = "UPDATE "+tableName
		statement += " SET "
		
		#columns = str2lst(columns)
		values = str2lst(values)
		values = listElem2str(values)
		values = quotize(values)
		if len(columns) is len(values):
			temp = []
			for elem in zip(columns, values):
				temp.append(join(elem," = "))
			statement += join(temp)
		else:
			raise ValueError, "ProgrammingError: different number of values"	
		
		if wcolumns is not False:
			#wcolumns = str2lst(wcolumns)
			wvalues = str2lst(wvalues)
			wvalues = listElem2str(wvalues)
			wvalues = quotize(wvalues)
			if len(wcolumns) is len(wvalues):
				statement += " WHERE "
				temp = []
				for elem in zip(wcolumns, wvalues):
					temp.append(join(elem, " "+logOp+" "))
				statement += join(temp," AND ")
			else:
				raise ValueError, "ProgrammingError: different number of values"	
		
		print statement
		#self.c.execute(statement)

	def delete(self, tableName, wcolumn, wvalue, logOp="="):
		statement = "DELETE FROM "+tableName+" WHERE "+wcolumn+" "+logOp+" "+str(wvalues)
		self.c.execute(statement)

	def select(self, tableNames, wcolumns=False, wvalues=False, logOp="=", columns=["*"], distinct=False):
		statement = "SELECT "
		if distinct: statement += "DISTINCT "
		columns = str2lst(columns)
		statement += join(columns)
		tableNames = str2lst(tableNames)
		statement += " FROM "+join(tableNames)
		if wcolumns is not False:
			wcolumns = str2lst(wcolumns)
			wvalues = str2lst(wvalues)
			wvalues = listElem2str(wvalues)
			wvalues = quotize(wvalues)
			if len(wcolumns) is len(wvalues):
				statement += " WHERE "
				temp = []
				for elem in zip(wcolumns, wvalues):
					temp.append(join(elem, " "+logOp+" "))
				statement += join(temp," AND ")
			else:
				raise ValueError, "ProgrammingError: different number of values"	
		print statement
		print "---"
#		self.c.execute(statement)
		

###		

path = "/home/procione/Scrivania/prociotools/database.db"
		
d = database(path)

tF =	[	
	["Field1", "VARCHAR(4)"],wcolumns = str2lst(wcolumns)
			wvalues = str2lst(wvalues)
			if len(wcolumns) is len(wvalues):
				statement += " WHERE "
				temp = []
				for elem in zip(wcolumns, wvalues):
					temp.append(join(elem, " "+logOp+" "))
				statement += join(temp," AND ")
			else:
				raise ValueError, "ProgrammingError: different number of values"	
	["Field2", "VARCHAR(8)"],
	["Field3", "INT"]
	]
	
#d.createTable("myTable",tF)
d.select("myTable","Field1", "ciao")
d.select(["myTable","altraTable"], "Field1","ciao","LIKE")
d.select("myTable", "Field2", "sono","=",distinct=True)
d.select("myTable", columns=["Field2","Field3"])

#d.insert("myTable", ["ciao","mammeta",7])
#d.insert("mytable", ["sono","almare",9])
#d.update("myTable", ["Field1", "Field2", "Field3"], ["ankr","xpoco",10], "Field1", "ciao")
#d.commit()

				
