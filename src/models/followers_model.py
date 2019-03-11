#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime

class FollowersModel:
        def __init__(self):
            conexion = pymongo.MongoClient('localhost',27017)
            self.db = conexion.instabot

        def setAllInactive(self):
            collection = self.db.followers;
            collection.update({},{'$set':{'active':False,'updated_at':datetime.now()}}, multi=True)

        def save(self, user_id, user_name):
            collection = self.db.followers
            result = collection.find({'user_id':str(user_id)})
            if result.count() == 0:
                follower = {'user_id':str(user_id),'user_name':user_name,'active':True,'created_at':datetime.now()}
                collection.insert_one(follower)
                return 1
            else:
                collection.update({'user_id':str(user_id)},{'$set':{'updated_at':datetime.now(),'active':True}})
                return 0;