#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime, timedelta

class FollowersModel:
        def __init__(self):
            conexion = pymongo.MongoClient('localhost',27017)
            self.db = conexion.instabot

        def setAllInactive(self):
            collection = self.db.followers;
            collection.update({'active':True},{'$set':{'active':False,'updated_at':datetime.now()}}, multi=True)

        def save(self, user_id, user_name):
            collection = self.db.followers
            result = collection.find({'user_id':str(user_id)})
            if result.count() == 0:
                follower = {'user_id':str(user_id),'user_name':user_name,'active':True,'created_at':datetime.now()}
                collection.insert_one(follower)
                return 1
            else:
                data = {'updated_at':datetime.now(),'active':True}
                collection.update({'user_id':str(user_id)},{'$set':data})
                return 0;

        def getNews(self, start, end):
            collection = self.db.followers
            return collection.find({'created_at': {'$gte': start, '$lt': end}})

        def getLost(self, start, end):
            collection = self.db.followers
            return collection.find({'active':False, 'updated_at': {'$gte': start, '$lt': end}})

        def getFollower(self, user_id):
            collection = self.db.followers
            return collection.find({'user_id':str(user_id),'active':True})

        def updateFollower(self, user_id, data):
            collection = self.db.followers
            collection.update({'user_id':str(user_id)},{'$set':data})
