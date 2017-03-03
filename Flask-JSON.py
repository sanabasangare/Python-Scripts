import json

import random

from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello_world():

    return 'Hello World!'


@app.route('/roll_dice/<int:sides>/json')
def dice_rolls():
    """This will return the result of the given number of rolls of a 6-sided die"""
	
    sides = 6

    # variable assigned, random.randint generate and return a random integer for die 1 & 2
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)

    # returning a sorted result in JSON
    return json.dumps({'die1': die1, 'die2': die2}, sort_keys = True)

if __name__ == '__main__':
    app.debug = True
    app.run()
