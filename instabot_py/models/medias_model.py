import pymongo

class MediasModel:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot

    def save(self, data):
        collection = self.db.medias;
        result = collection.find({'id':data['id']});
        if result.count() == 0:
            collection.insert_one(data)
            return 1
        else:
            collection.update({'id':data['id']},{'$set':data})
            return 0

    def saveLikers(self, media_id, data_liker):
        collection = self.db.likers
        data_liker['media_id'] = media_id
        result = collection.find({'media_id':data_liker['media_id']})
        if result.count() == 0:
            collection.insert_one(data_liker)
        else:
            collection.update({'media_id':result[0]['media_id']},{'$set':data_liker})

