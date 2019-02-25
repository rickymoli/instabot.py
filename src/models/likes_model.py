#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime

class LikesModel:
        def __init__(self):
            conexion = pymongo.MongoClient('localhost',27017)
            self.db = conexion.instabot

        def save(self, user_id, tag):
            collection = self.db.likes
            like = {'user_id':user_id,'tag':tag,'created_at':datetime.now()}
            return collection.insert_one(like).inserted_id
