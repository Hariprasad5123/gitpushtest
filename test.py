import pymongo

client = pymongo.MongoClient("mongodb+srv://root:system@cluster0.zhurd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

details = {
    "Surname" : "Anna",
    "Firstname" : "Hari",
    "Lastname" : "Prasad",
    "Email" : "annahari.ram97@gmail.com"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(details)

