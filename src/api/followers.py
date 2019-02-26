from InstagramAPI import InstagramAPI
import sys
sys.path.insert(0, '../models')
from followers_model import FollowersModel

def getTotalFollowers(api, user_id):
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

followers_model = FollowersModel();
InstagramAPI = InstagramAPI("", "")
InstagramAPI.login()
user_id = InstagramAPI.username_id
followers = getTotalFollowers(InstagramAPI, user_id)
followers_model.setAllInactive()
new = 0
for item in followers:
    new += followers_model.save(item['pk'], item['username'])
print 'New followers: ' + str(new)
