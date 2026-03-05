
# import data_sheet
# data = data_sheet.data


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# from dotenv import load_dotenv
# import os
# from pymongo import MongoClient

# load_dotenv()

# uri = os.getenv("MONGO_URI")

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
# # 
# # =================================
# # db = client["five-dollar"]           # the name of database
# # collection = db["gift-collection"]   # the name of collection

# # WRITE (inser one document)

# # for item in data:                    # retrieve data (list of dictionaries) from five_dollar_app.py
# #     collection.insert_one(item)

# # Finished adding all current items into cloud database. Don't want to reduplicate adding them. 

# # print("Successfully insert all items into database.")

# # READ (find one document)
# doc = collection.find_one({"price": 3.39})
# print(doc)

# doc = collection.find_one({"name": "Post-it Sticky Notes"})
# print(doc)

# for gift in collection.find():
#     print(gift)

