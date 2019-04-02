import pymongo
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/home/pi/develop/instabot.py/instabot_py/models')
from consolidate_model import ConsolidateModel

class AddInteractionsConsolidation:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot

    def getInteractions(self, tag, start, end):
        interactions = 0
        interactions += self.db.follows.find({'tag':tag, 'created_at': {'$gte': start, '$lt': end}}).count()
        interactions += self.db.comments.find({'tag':tag, 'created_at': {'$gte': start, '$lt': end}}).count()
        interactions += self.db.likes.find({'tag':tag, 'created_at': {'$gte': start, '$lt': end}}).count()
        return interactions

    def execute(self, start, end):
        date = start.strftime("%Y-%m-%d")
        consolidate_model = ConsolidateModel()
        tags = consolidate_model.getTagsByDate(date)
        for tag in tags:
            interactions = self.getInteractions(tag['name'], start, end)
            consolidate_model.updateTags({'name':tag['name'], 'date':date},{'interactions':interactions})
