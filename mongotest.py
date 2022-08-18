import pymongo

client = pymongo.MongoClient("mongodb+srv://shivaraj:Shivaraj123@cluster0.ijjrr9m.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"shivaraj",
    "address":"choutagi",
    "uru":"hosaritti_le"
}
db2=client['mongotest']
coll=db2['test']
coll.insert_one(d)




