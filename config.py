import pymongo
import certifi

uri = "mongodb+srv://fsdi:rooter32@cluster0.q0t28gv.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri, tlsCAFile = certifi.where())
db = client.get_database("organika") # could be another schema name