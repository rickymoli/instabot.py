#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime

class CommentsModel:
        def __init__(self):
            conexion = pymongo.MongoClient('localhost',27017)
            self.db = conexion.instabot

        def save(self, user_id, text, tag, media_id):
            collection = self.db.comments
            comment = {'user_id':user_id,'text':text,'tag':tag,'media_id':media_id,'created_at':datetime.now()}
            return collection.insert_one(comment).inserted_id

        def getTags(self, start, end):
            collection = self.db.comments
            items = collection.aggregate([
                {'$match':{'created_at':{'$gte':start,'$lt':end}}},
                {'$group':{'_id':'$tag','tag':{'$last':'$tag'}}}
            ]);
            return list(items)

        def getByUserId(self, user_id):
            collection = self.db.comments
            return collection.find({'user_id': user_id})
