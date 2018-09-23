# Team Uhm Hui Min Wu and Cheryl Qian
# SoftDev1 pd08
# K10 -- Jinja Tuning
# 2018-09-23

from flask import Flask, render_template
import random
import csv

app = Flask(__name__)

dict = {}
with open('data/occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dict[row['Job Class']] = float(row['Percentage'])
    del dict['Total']
    print(dict)

def randomOcc():
    randomselect = random.uniform(0,99.8)
    for x in dict:
        randomselect = randomselect - dict[x]
        if (randomselect <= 0):
            return x;


@app.route("/occupations")
def occupation():
    return render_template('template.html',
                    title = 'Occupations',
                    heading = 'Below shows the percentages of Americans with the corresponding job. You''ll also get a random job generated with the percentages as the probability.',
                    collection = dict,
                    text = 'Job: ' + randomOcc())


if __name__ == "__main__":
    app.debug = True
    app.run()

