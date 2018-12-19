#Hui Min Wu and Thomas Zhao Team zhao-wu-mama
#SoftDev1 pd8
#K16 -- No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
def createStuds():
    
    command = "CREATE TABLE peps (name TEXT, age INTEGER, id INTEGER)" #creates table called peps with those parameters
    c.execute(command) #executes the command above

    with open('raw/peeps.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            command0 = "INSERT INTO peps VALUES (\"" + row['name'] + "\"," + row['age'] + "," + row['id'] + ")"
            c.execute(command0)

def createCourses():

    command = "CREATE TABLE coarses (code TEXT, mark INTEGER, id INTEGER)"
    c.execute(command)

    with open('raw/courses.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            command0 = "INSERT INTO coarses VALUES (\"" + row['code'] + "\"," + row['mark'] + "," + row['id'] + ")"
            c.execute(command0)


createStuds()
createCourses()
#==========================================================

db.commit() #save changes
db.close()  #close database


