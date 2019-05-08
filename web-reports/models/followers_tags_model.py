import pymongo

class FollowersTagsModel:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot
        self.collection = self.db.consolidate_followers_tags

    def getBestTags(self, date):
        tags = self.collection.aggregate([
            {'$match':{'date':{'$gte':date}}},
            {'$group':{
                '_id':'$name',
                'new':{'$sum':'$new'},
                'lost':{'$sum':'$lost'},
                'interactions':{'$sum':'$interactions'},
            }},
            {'$project':{
                '_id':1,
                'growth': {'$subtract':['$new','$lost']},
                'interactions': 1
            }},
            {'$match':{'growth':{'$gt':0}}},
            {'$project':{
                '_id': 1,
                'growth': 1,
                'interactions': 1,
                'accurate': {'$multiply': [100, {'$divide':['$growth', '$interactions']}]}
            }},
            {'$sort': {'accurate': -1}}
        ])
        return list(tags)

    def getWorstTags(self, date):
        tags = self.collection.aggregate([
            {'$match':{'date':{'$gte':date}}},
            {'$group':{
                '_id':'$name',
                'new':{'$sum':'$new'},
                'lost':{'$sum':'$lost'},
                'interactions':{'$sum':'$interactions'},
            }},
            {'$project':{
                '_id':1,
                'growth': {'$subtract':['$new','$lost']},
                'interactions': 1
            }},
            {'$match':{'growth':{'$lte':0}}},
            {'$project':{
                '_id': 1,
                'interactions': 1
            }},
            {'$sort': {'interactions': -1}}
        ])
        return list(tags)
