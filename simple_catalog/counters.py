from pymongo import MongoClient
from django.conf import settings

class AnimalCounter:
  def __init__(self):
    self.client = self.get_mongo_client()
  def get_mongo_client(self):
    mongo_uri = settings.MONGO_URI
    client = MongoClient(mongo_uri)
    return client

  def increase_animal_count(self, user):
    db = self.client.get_default_database()
    animal_count_collection = db.animal_counts
    animal_count_document = animal_count_collection.find_one({"user": user})
    if animal_count_document:
      animal_count_collection.update_one({"user": user}, {"$inc": {"total_animal": 1}})
    else:
      animal_count_collection.insert_one({"user": user, "total_animal": 1})

  def decrease_animal_count(self, user):
    db = self.client.get_default_database()
    animal_count_collection = db.animal_counts
    animal_count_document = animal_count_collection.find_one({"user": user})
    if animal_count_document and animal_count_document["total_animal"] > 0:
      animal_count_collection.update_one({"user": user}, {"$inc": {"total_animal": -1}})

  def animal_count(self, user):
    db = self.client.get_default_database()
    animal_count_collection = db.animal_counts
    animal_count_document = animal_count_collection.find_one({"user": user})
    if animal_count_document:
      return animal_count_document["total_animal"]
    else:
      return 0

  def animal_count_all(self):
    db = self.client.get_default_database()
    animal_count_collection = db.animal_counts
    all_data = list(animal_count_collection.find())
    return all_data
