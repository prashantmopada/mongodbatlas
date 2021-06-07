from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route('/conn_mongo',methods=['POST'])
def cloud_mongo_connect():
    if request.method =='POST':
        try:
            client = pymongo.MongoClient("mongodb+srv://Robin:1986@cluster0.7rltc.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
            db = client.test
        except exception as e: print(e)
        return "welcome to Mongodb"

@app.route('/create_collection',methods=['POST'])
def create_collection_one():
    if request.method=='POST':
        try:
            client = pymongo.MongoClient("mongodb+srv://Robin:1986@cluster0.7rltc.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
            mydb = client['myFirstDatabase']
            my_collection = mydb['Customers']

            mydict = { "name": "Dakota Johnson", "address": "LA 37" }
            my_collection.insert_one(mydict)

        except exception as e: print(e)
        return "Collection created"

@app.route('/insert_into_collec_many',methods=['POST'])
def create_collection_many():
    if request.method=='POST':
        try:
            client = pymongo.MongoClient("mongodb+srv://Robin:1986@cluster0.7rltc.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
            mydb = client['myFirstDatabase']
            my_collection = mydb['Companies']
            mydict1=([{'Company': 'Renault', 'Vacancy': 10}, {'Company': 'Ford', 'Vacancy': 15}, {'Company': 'Nissan', 'Vacancy': 25},
                                   {'Company': 'Toyota', 'Vacancy': 100}, {'Company': 'Hyundai', 'Vacancy': 5}])

            my_collection.insert_many(mydict1)
        except exception as e: print(e)
        return "Many records inserted"


if __name__ == "__main__":
    app.run(debug=True)


