from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.Filedb
file = db.files

# post = [{"author": "Shelly",
#          "text": "My first blog post!"
#          },
#         {"author": "Lucy",
#          "text": "Mongo db blog"
#          }]

# post_ins = posts.insert_many(post)
# post_id = posts.insert_one(post).inserted_id
# print(db.list_collection_names(), post_id)


