import pymongo
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/home/pi/develop/instabot.py/instabot_py/models')
from followers_model import FollowersModel
from likes_model import LikesModel
from follows_model import FollowsModel
from comments_model import CommentsModel
from consolidate_model import ConsolidateModel

class FollowersConsolidation:
    def execute(self, start, end):
        consolidate_model = ConsolidateModel()
        followers_model = FollowersModel()
        yesterday = start
        yesterday_start = start
        yesterday_end = end

        followers_news = followers_model.getNews()
        followers_lost = followers_model.getLost(yesterday_start, yesterday_end)
        date = yesterday.strftime("%Y-%m-%d")
        consolidate_model.saveFollowers(date, followers_news.count(), followers_lost.count())

        tags = []
        likes_model = LikesModel()
        likes_tags = likes_model.getTags(yesterday_start, yesterday_end)
        for likes_tag in likes_tags:
            tags.append(likes_tag['tag'])

        comments_model = CommentsModel()
        comments_tags = comments_model.getTags(yesterday_start, yesterday_end)
        for comments_tag in comments_tags:
            if (comments_tag['tag'] not in tags):
                tags.append(comments_tag['tag'])

        follows_model = FollowsModel()
        follows_tags = follows_model.getTags(yesterday_start, yesterday_end)
        for follows_tag in follows_tags:
            if (follows_tag['tag'] not in tags):
                tags.append(follows_tag['tag'])

        for i, tag in enumerate(tags):
            tags[i] = {'name': tag, 'date': date, 'likes_new': 0, 'likes_lost': 0, 'comments_new': 0, 'comments_lost': 0, 'follows_new': 0, 'follows_lost': 0, 'new': 0, 'lost': 0};

        for follower_new in followers_news:
            r = likes_model.getByUserId(follower_new['user_id'])
            if r.count() > 0:
                for i, tag in enumerate(tags):
                    if tag['name'] == r[0]['tag']:
                        tags[i]['likes_new'] += 1
                        tags[i]['new'] += 1
            else:
                r = comments_model.getByUserId(follower_new['user_id'])
                if r.count() > 0:
                    for i, tag in enumerate(tags):
                        if tag['name'] == r[0]['tag']:
                            tags[i]['comments_new'] += 1
                            tags[i]['new'] += 1
                else:
                    r = follows_model.getByUserId(follower_new['user_id'])
                    if r.count() > 0:
                        for i, tag in enumerate(tags):
                            if tag['name'] == r[0]['tag']:
                                tags[i]['follows_new'] += 1
                                tags[i]['new'] += 1

        for follower_lost in followers_lost:
            r = likes_model.getByUserId(follower_lost['user_id'])
            if r.count() > 0:
                for i, tag in enumerate(tags):
                    if tag['name'] == r[0]['tag']:
                        tags[i]['likes_lost'] += 1
                        tags[i]['lost'] += 1
            else:
                r = comments_model.getByUserId(follower_lost['user_id'])
                if r.count() > 0:
                    for i, tag in enumerate(tags):
                        if tag['name'] == r[0]['tag']:
                            tags[i]['comments_lost'] += 1
                            tags[i]['lost'] += 1
                else:
                    r = follows_model.getByUserId(follower_lost['user_id'])
                    if r.count() > 0:
                        for i, tag in enumerate(tags):
                            if tag['name'] == r[0]['tag']:
                                tags[i]['follows_lost'] += 1
                                tags[i]['lost'] += 1

        consolidate_model.saveFollowersTag(tags)
