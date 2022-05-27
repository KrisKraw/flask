#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import jsonify


houseWives = [
                {"name" : "Teresa Giudice",
                  "spouse" : "Luis Ruelas",
                  "spousestatus" : "fiance",
                  "photoUrl" : "https://i.insider.com/625734a61ab4020019279e04?width=1000&format=jpeg&auto=webp",
                  "hometown" : "Montville",
                  "age" : "42",
                  "numofchildren" : "4",
                },
                {"name" : "Melissa Gorga",
                  "spouse" : "Joe",
                  "spousestatus" : "husband",
                  "photoUrl" : "https://m.media-amazon.com/images/M/MV5BMjE4NDk3NDE3M15BMl5BanBnXkFtZTcwNDk5NDQwOA@@._V1_.jpg",
                  "hometown" : "Franklin Lakes, NJ",
                  "age" : "43",
                  "numofchildren" : "3",
                },
                {"name" : "Jennifer Aydin",
                  "spouse" : "Dr. Bill Aydin",
                  "spousestatus" : "husband",
                  "photoUrl" : "https://www.cheatsheet.com/wp-content/uploads/2021/03/jenniferaydin-rhonj-bravo.jpg",
                  "hometown" : "Paramus, NJ",
                  "age" : "45",
                  "numofchildren" : "5",
                },
                {"name" : "Jackie Goldschneider",
                  "spouse" : "Evan",
                  "spousestatus" : "husband",
                  "photoUrl" : "https://media.distractify.com/brand-img/2ydPNZhjW/0x0/jackie-goldschneider-1651702442199.jpg",
                  "hometown" : "Tenafly",
                  "age" : "44",
                  "numofchildren" : "4",
                },
                {"name" : "Dolores Catania",
                  "spouse" : "",
                  "spousestatus" : "single",
                  "photoUrl" : "https://www.newbeauty.com/wp-content/uploads/2021/02/real-housewives-plastic-surgery-1024x736.png",
                  "hometown" : "Monvale, NJ",
                  "age" : "51",
                  "numofchildren" : "2",
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
