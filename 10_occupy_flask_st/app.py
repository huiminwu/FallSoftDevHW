# Team Uhm Hui Min Wu and Cheryl Qian
# SoftDev1 pd08
# K10 -- Jinja Tuning
# 2018-09-23

from flask import Flask, render_template
import random
import csv
import getOccupation

app = Flask(__name__)

@app.route("/occupations")
def occupation():
    return render_template('template.html',
                    title = 'Occupations',
                    heading = 'Below shows the percentages of Americans with the corresponding job. You''ll also get a random job generated with the percentages as the probability.',
                    collection = getOccupation.generateDict(),
                    text = 'Job: ' + getOccupation.randomOccupation())


if __name__ == "__main__":
    app.debug = True
    app.run()

