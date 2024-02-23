import pymongo
import certifi

uri = "mongodb+srv://admin0:1234admin@cluster0.vypjbc9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri, tlsCAFile = certifi.where())
db = client.get_database("organika") # could be another schema name