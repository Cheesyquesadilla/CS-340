#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    #Access Mongodb for AAC file
    def __init__(self,username,password):
        self.client = MongoClient('mongodb://%s:%s@localhost:31461/?authMechanism=DEFAULT&authSource=AAC'%(username,password))
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
    #CRUD Operationstions
    def create(self, data): 
        if data is not None:
            self.database.animals.insert_one(data)
            return True    
        else:
            raise Exception("Data parameter is empty")
            return False
            
    def read(self, readData=None):
        if readData is not None:
            return self.database.animals.find(readData, {"_id": False})
        else:
            raise Exception("List Empty")
            return False

    def update(self, updateData):
        if updateData is not None:
            if updateData:
                self.database.animals.insert(updateData)
            
        else:
            raise Exception("No data to update")
        
    def delete(self, deleteData):
       if deleteData is not None:
            if deleteData:
                self.database.animals.delete(deleteData)
                return True
       else:
            raise Exception("No data to delete")
            return False