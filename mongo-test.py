
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("MongoDB Test. Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# =================================
db = client["five-dollar"]           # the name of database
collection = db["gift-collection"]   # the name of collection

# WRITE (inser one document)
collection.insert_one({
        "name" : "Spiral Notebook",
        "price": 3.39,
        "image_url": "https://img-1.kwcdn.com/product/open/34273584381743a98021073c1a1c725b-goods.jpeg?imageView2/2/w/264/q/70/format/avif"
    })


# READ (find one document)
doc = collection.find_one({"price": 3.39})
print(doc)

