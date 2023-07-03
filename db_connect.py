from flask import flash
import pymongo
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

password=os.environ.get("MONGODB_PWD")
if password:
    client = pymongo.MongoClient(f"mongodb+srv://mkt:{password}@cluster0.08qlmav.mongodb.net/colleges?retryWrites=true&w=majority",maxPoolSize=50,connect=False)
def db_connection():
    try:
        db = pymongo.database.Database(client,"colleges")
        print(db.list_collection_names())
        col=pymongo.collection.Collection(db,'students')
        
        print(col)
        return col
    except:
        flash("Server not avialable",'error')
        print("Server not available")

