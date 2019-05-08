import pymongo

class FollowersModel:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot
        self.collection = self.db.consolidate_followers

    def getGrowth(self, date):
        items = self.collection.aggregate([
            {'$match': {'date':{'$gte':date}}},
            {'$project': {
                'date': 1,
                'growth': {'$subtract': ['$news','$lost']},
                'growth_tags': {'$subtract': ['$tags_new','$tags_lost']},
                'growth_medias': {'$subtract': ['$medias_new','$medias_lost']}
            }},
            {'$sort':{'date':1}}
        ])
        return list(items)

    def getFirstDate(self):
        item = self.collection.find({}).sort('date',pymongo.ASCENDING)
        if item.count() > 0:
            return item[0]['date']
        else:
            return ''
