#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#c.execute("CREATE TABLE peps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")

with open('../../raw/peeps.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:

		theList = (row['name'], row['age'], row['id']) 
		c.execute("INSERT INTO peps VALUES (?,?,?)", theList)
command = ""          #build SQL stmt, save as string
c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


