from app import app, db
import csv
import flask

from app.models import DogBreeds




@app.route('/')
@app.route('/index')
def index(): 
    message = { "hello":"world"}
    return flask.jsonify(message)

@app.route('/load')
def load_resources():
    with open('app/dogweight.csv', 'rt') as dogweightcsv: #open csv
        reader = csv.reader(dogweightcsv, delimiter=",")    #load each row as an instance (dataitem) of dogbreedclass
        print(reader)
        next(reader, None)  # skip the headers
        for row in reader:
            data = DogBreeds(id=row[0], breedname=row[1], minweight=row[2], maxweight=row[3])
            db.session.add(data)
        return "Resources loaded.  There are now %i resources into the database." % db.session.query(DogBreeds).count()
        db.session.commit()
    
#def getbreeds():
#    for line in db:
        
        
