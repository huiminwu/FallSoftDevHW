#Hui Min Wu and Maryann Foley Team Lil Peeps
#SoftDev1 pd8
#K17 -- Average
#2018-10-05

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
            c.execute("INSERT INTO peps VALUES (\" {0} \", {1}, {2})".format(row["name"], row["age"], row["id"]))


def createCourses():

    command = "CREATE TABLE coarses (code TEXT, mark INTEGER, id INTEGER)"
    c.execute(command)

    with open('raw/courses.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute("INSERT INTO coarses VALUES (\" {0} \", {1}, {2})".format(row["code"], row["mark"], row["id"]))
def lookUp():
    c.execute("SELECT name, peps.id, mark FROM peps, coarses WHERE peps.id = coarses.id")
    print(c.fetchall())

def average(printTF=False):
    retList=[]
    for i in range(1,11):
        total=0
        numOfMarks=0
        name=""
        c.execute("SELECT mark,name FROM coarses,peps WHERE coarses.id = peps.id AND peps.id = "+ str(i))
        for row in c:
            total+=row[0]
            numOfMarks+=1
            name=row[1]
        avg=total/numOfMarks
        if printTF:
            print(name,i,avg)
        retList.append([i,avg])
    return retList

def createAverage():
    c.execute("CREATE TABLE peeps_avg (id INTEGER,avg NUMBER)")
    avgs=average(True)
    for avg in avgs:
        c.execute("INSERT INTO peeps_avg VALUES (?,?)",avg)

def newCourse(course,mark,id):
    c.execute("INSERT INTO coarses VALUES (\" {0} \", {1}, {2})".format(course, mark, id))
    recalculateAvgs()

def recalculateAvgs():
    for i in range(1,11):
        c.execute("DELETE FROM peeps_avg WHERE peeps_avg.id = "+str(i))
    avgs=average()
    for avg in avgs:
        c.execute("INSERT INTO peeps_avg VALUES (?,?)",avg)

createStuds()
createCourses()
lookUp()
print("==================OLD AVERAGES================")
createAverage()
newCourse("wood",71,9)
newCourse("woof",0,1)
newCourse("woog",7,2)
newCourse("woop",900,3)
newCourse("woow",78,4)
newCourse("woom",694,5)
newCourse("woor",666,6)
newCourse("wooa",21,7)
newCourse("wooo",8,8)
newCourse("wooe",777777,10)
print("=================NEW AVERAGES=================")
average(True)
#==========================================================

db.commit() #save changes
db.close()  #close database
