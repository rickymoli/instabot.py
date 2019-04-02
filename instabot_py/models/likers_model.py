import pymongo

class LikersModel:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot

    def get(self, start, end):
        collection = self.db.likers
        likers = collection.aggregate([
            {'$unwind':'$users'},
            {'$match':{'users.created_at':{'$gte': start, '$lt': end}}},
            {'$sort':{'users.created_at':1}},
            {'$group':{'_id':'$users.pk','pk':{'$last':'$users.pk'},'media_id':{'$first':'$media_id'},'created_at':{'$first':'$users.created_at'}}}
        ])
        return list(likers)

    def isLiker(self, pk, start, end):
        collection = self.db.likers
        items = collection.find({'users':{'$elemMatch':{'pk':int(pk),'created_at':{'$gte':start,'$lt':end}}}})
        if items.count() > 0:
            return True
        else:
            return False
