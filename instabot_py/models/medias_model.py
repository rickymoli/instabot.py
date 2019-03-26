import pymongo

class MediasModel:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot

    def save(self, data, now):
        collection = self.db.medias;
        result = collection.find({'id':data['id']});
        if result.count() == 0:
            data['created_at'] = now
            collection.insert_one(data)
            return 1
        else:
            data['updated_at'] = now
            collection.update({'id':data['id']},{'$set':data})
            return 0

    def saveLikers(self, media_id, data_liker, now):
        collection = self.db.likers
        data_liker['media_id'] = media_id
        result = collection.find({'media_id':data_liker['media_id']})
        if result.count() == 0:
            for i, user in enumerate(data_liker['users']):
                data_liker['users'][i]['created_at'] = now
            collection.insert_one(data_liker)
        else:
            for i, item in enumerate(data_liker['users']):
                user = collection.find({'media_id':data_liker['media_id'],'users': {'$elemMatch':{'pk':item['pk']}}})
                if user.count() == 0:
                    data_liker['users'][i]['created_at'] = now
                    collection.update({'media_id':data_liker['media_id']},{'$push':{'users':data_liker['users'][i]}})
