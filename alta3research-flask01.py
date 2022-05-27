#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import jsonify


houseWives = [
                {'name' : 'Teresa Giudice',
                  'spouse' : 'Luis Ruelas',
                  'spousestatus' : 'fiance',
                  'photoUrl' : 'https://i.insider.com/625734a61ab4020019279e04?width=1000&format=jpeg&auto=webp',
                  'hometown' : 'Montville',
                  'age' : '10/14/1967',
                  'numofchildren' : '4',
                },
                {'name' : 'Melissa Gorga',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photoUrl' : '',
                  'hometown' : '',
                  'age' : '',
                  'numofchildren' : '',
                },
                {'name' : 'Jennifer Aydin',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photoUrl' : '',
                  'hometown' : '',
                  'age' : '',
                  'numofchildren' : '',
                },
                {'name' : 'Jackie Goldschneider',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photoUrl' : '',
                  'hometown' : '',
                  'age' : '',
                  'numofchildren' : '',
                },
                {'name' : 'Dolores Catania',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photoUrl' : '',
                  'hometown' : '',
                  'age' : '',
                  'numofchildren' : '',
                },
                {'spouse' : 'Luis Ruelas',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photoUrl' : '',
                  'hometown' : '',
                  'age' : '',
                  'numofchildren' : '',
                }
            ]


app = Flask(__name__)


#a webpage with biographies of the current RHONJ housewives
@app.route("/")
def webpage():
    return render_template("housewives.html", houseWives = houseWives)


#an api that returns all of the RHONJ data in JSON format
#data validated with https://jsonlint.com/
@app.route("/api")
def api():
    data = jsonify(houseWives)
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
