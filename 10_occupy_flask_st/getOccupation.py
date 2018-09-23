# Team InZane HuiMins - Hui Min Wu and Zane Wang
# SoftDev1 pd8
# K06 -- Stl/O: Divine your Destiny!
# 2018-09-13

import random
import csv

def generateDict():
    dict = {}
    with open('data/occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile) #using dictreader instead of reader allows us to be able to pass parameters from the 1st row to create dict
        for row in reader:
            dict[row['Job Class']] = float(row['Percentage'])
        del dict['Total']
        #testing: print(dict)
    return dict

def randomOccupation():
    dict = generateDict()
    randomselect = random.uniform(0, 99.8) #returns a random floating point number including 0 and 99.8
    #testing: print (randomselect)
    for x in dict:
        randomselect = randomselect - dict[x]
        if (randomselect <= 0):
            return x

