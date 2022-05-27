#!/usr/bin/env python3


houseWives = [
                {'name' : 'Teresa Giudice',
                  'spouse' : 'Luis Ruelas',
                  'spousestatus' : 'fiance',
                  'photo' : 'https://i.insider.com/625734a61ab4020019279e04?width=1000&format=jpeg&auto=webp',
                  'hometown' : 'Montville',
                  'dob' : '10/14/1967',
                  'numofchildren' : '4',
                },
                {'name' : 'Melissa Gorga',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photo' : '',
                  'hometown' : '',
                  'dob' : '',
                  'numofchildren' : '',
                },
                {'name' : 'Jennifer Aydin',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photo' : '',
                  'hometown' : '',
                  'dob' : '',
                  'numofchildren' : '',
                },
                {'name' : 'Jackie Goldschneider',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photo' : '',
                  'hometown' : '',
                  'dob' : '',
                  'numofchildren' : '',
                },
                {'name' : 'Dolores Catania',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photo' : '',
                  'hometown' : '',
                  'dob' : '',
                  'numofchildren' : '',
                },
                {'spouse' : 'Luis Ruelas',
                  'spouse' : '',
                  'spousestatus' : '',
                  'photo' : '',
                  'hometown' : '',
                  'dob' : '',
                  'numofchildren' : '',
                }
            ]


#a webpage with biographies of the current RHONJ housewives
@app.route("/")
def start():
    return render_housewifes("housewives.html")

#an api that returns all of the RHONJ data in JSON format
#//https://jsonlint.com/
@app.route("/api")
def api():
    return f"your answer was correct !"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE