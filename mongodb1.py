import pymongo

client = pymongo.MongoClient('localhost')

db = client['test_db']

collect = db['test_collect']

#collect.insert({'name':'dddddcc','age':20,'_id':1})

#查



for row in collect.find():
    print(row['name'])
