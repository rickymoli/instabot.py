#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime

class FollowsModel:
        def __init__(self):
            conexion = pymongo.MongoClient('localhost',27017)
            self.db = conexion.instabot

        def save(self, user_id, tag):
            collection = self.db.follows
            follow = {'user_id':user_id,'tag':tag,'created_at':datetime.now()}
            return collection.insert_one(follow).inserted_id
