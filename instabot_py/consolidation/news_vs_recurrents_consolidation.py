import pymongo
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/home/pi/develop/instabot.py/instabot_py/models')
from likers_model import LikersModel
from followers_model import FollowersModel
from consolidate_model import ConsolidateModel

class NewsVsRecurrentsConsolidation:
    def __init__(self):
        conexion = pymongo.MongoClient('localhost',27017)
        self.db = conexion.instabot

    def getInteractions(self, user_id):
        if self.db.follows.find({'user_id':str(user_id)}).count() > 0:
            return self.db.follows.find({'user_id':str(user_id)})
        elif self.db.comments.find({'user_id':str(user_id)}).count() > 0:
            return self.db.comments.find({'user_id':str(user_id)})
        else:
            return self.db.likes.find({'user_id':str(user_id)})

    def execute(self, start, end):
        likers_model = LikersModel()
        followers_model = FollowersModel()
        consolidate_model = ConsolidateModel()
        likers = likers_model.get(start, end)
        date = start.strftime("%Y-%m-%d")
        consolidate_model.removeFollowersMedia(date)
        for liker in likers:
            follower = followers_model.getFollower(liker['pk'])
            if follower.count() > 0:
                if 'updated_at' in follower[0]:
                    is_new = False
                else:
                    is_new = True
                tag_interaction = ''
                if 'tag_interaction' in follower[0]:
                    tag_interaction = follower[0]['tag_interaction']
                else:
                    interaction = self.getInteractions(liker['pk'])
                    if interaction.count() > 0:
                        tag_interaction = interaction[0]['tag']
                        followers_model.updateFollower(follower[0]['user_id'],{'tag_interaction':tag_interaction})
                if tag_interaction != '':
                    if is_new == True:
                        consolidate_model.addNewFollowersTag(tag_interaction, date, 1)
                    else:
                        consolidate_model.addRecurrentFollowersTag(tag_interaction, date, 1)
                else:
                    if is_new == True:
                        consolidate_model.addNewFollowersMedia(liker['media_id'], date, 1)
                    else:
                        consolidate_model.addRecurrentFollowersMedia(liker['media_id'], date, 1)
                if is_new != True:
                    consolidate_model.addLikerRecurrentFollowers(date, 1)
