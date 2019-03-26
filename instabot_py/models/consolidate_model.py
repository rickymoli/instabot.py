#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

class ConsolidateModel:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot

    def saveFollowers(self, date, news, lost):
        collection = self.db.consolidate_followers
        collection.remove({'date':date})
        collection.insert_one({'date':date,'news':news,'lost':lost})

    def addLikerRecurrentFollowers(self, date, num):
        collection = self.db.consolidate_followers
        item = collection.find({'date':date})
        if item.count() > 0:
            if 'likers_recurrent' in item[0]:
                num = item[0]['likers_recurrent'] + num
            collection.update({'date':date},{'$set':{'likers_recurrent':num}})

    def saveFollowersTag(self, data):
        collection = self.db.consolidate_followers_tags
        collection.remove({'date':data[0]['date']}, multi=True)
        collection.insert_many(data)

    def addNewFollowersTag(self, tag, date, num):
        collection = self.db.consolidate_followers_tags
        item = collection.find({'name':tag,'date':date})
        if item.count() > 0:
            fields = {'likers_new':0,'likers_recurrent':0}
            if 'likers_new' in item[0]:
                fields['likers_new'] = item[0]['likers_new'] + num
            else:
                fields['likers_new'] = num
            if 'likers_recurrent' in item[0]:
                fields['likers_recurrent'] = item[0]['likers_recurrent']
            collection.update({'name':tag,'date':date},{'$set':fields})

    def addRecurrentFollowersTag(self, tag, date, num):
        collection = self.db.consolidate_followers_tags
        item = collection.find({'name':tag,'date':date})
        if item.count() > 0:
            fields = {'likers_new':0,'likers_recurrent':0}
            if 'likers_recurrent' in item[0]:
                fields['likers_recurrent'] = item[0]['likers_recurrent'] + num
            else:
                fields['likers_recurrent'] = num
            if 'likers_new' in item[0]:
                fields['likers_new'] = item[0]['likers_new']
            collection.update({'name':tag,'date':date},{'$set':fields})

    def addNewFollowersMedia(self, media_id, date, num):
        collection = self.db.consolidate_followers_medias
        item = collection.find({'media_id':media_id,'date':date})
        if item.count() > 0:
            fields = {'new':0,'recurrent':0}
            if 'new' in item[0]:
                fields['new'] = item[0]['new'] + num
            else:
                fields['new'] = num
            if 'recurrent' in item[0]:
                fields['recurrent'] = item[0]['recurrent']
            collection.update({'media_id':media_id,'date':date},{'$set':fields})
        else:
            collection.insert({'media_id':media_id,'date':date,'new':num,'recurrent':0})

    def addRecurrentFollowersMedia(self, media_id, date, num):
        collection = self.db.consolidate_followers_medias
        item = collection.find({'media_id':media_id,'date':date})
        if item.count() > 0:
            fields = {'new':0,'recurrent':0}
            if 'recurrent' in item[0]:
                fields['recurrent'] = item[0]['recurrent'] + num
            else:
                fields['recurrent'] = num
            if 'new' in item[0]:
                fields['new'] = item[0]['new']
            collection.update({'media_id':media_id,'date':date},{'$set':fields})
        else:
            collection.insert({'media_id':media_id,'date':date,'new':0,'recurrent':num})

    def removeFollowersMedia(self, date):
        collection = self.db.consolidate_followers_medias
        collection.remove({'date':date}, multi=True)
