from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from routes import create_bolt
from models import Bolt

import csv

uri = "mongodb+srv://Vonalzo:fPMXNUkXA4REyhCa@cluster0.qlfwyae.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['pelda']
posts = db.posts

boltcollection = db['vasarlas']

csvFile = open('vasarlas.csv', 'r')
reader = csv.DictReader(csvFile)

header = reader.fieldnames

for each in reader:
    row = {}
    for field in header:
        if(field == "esemenydatumido"):
            row[field] = each[field]
        else:
            row[field] = int(each[field])
    try:
        x = boltcollection.insert_one(row)
        print(x)
    except:
        pass