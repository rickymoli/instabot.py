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
InstagramAPI = InstagramAPI("david.plancton", "apachito")
InstagramAPI.login()
user_id = InstagramAPI.username_id
followers = getTotalFollowers(InstagramAPI, user_id)
followers_model.setAllInactive()
new = 0
for item in followers:
    new += followers_model.save(item['pk'], item['username'])
#print "New followers: " + str(new)


#var follower_from_comments = 0;
#var follower_from_follows = 0;
#var follower_from_likes = 0;
#db.followers.find({active : true}).forEach( function(follower){
#    if (db.comments.find({user_id : follower.user_id}).count() > 0){
#        follower_from_comments = follower_from_comments + 1;
#    }
#    if (db.follows.find({user_id : follower.user_id}).count() > 0){
#        follower_from_follows = follower_from_follows + 1;
#    }
#    if (db.likes.find({user_id : follower.user_id}).count() > 0){
#        follower_from_likes = follower_from_likes + 1;
#    }
#});
#print("follower_from_comments = " + follower_from_comments);
#print("follower_from_follows = " + follower_from_follows);
#print("follower_from_likes = " + follower_from_likes);

#db.followers.find({active : false}).forEach((it)=> { 
#    var follower = it.user_id;
#    if (db.follows.find({user_id : follower}).count()>0){
#        print(it.user_name + " found in follows");
#    }
#    if (db.comments.find({user_id : follower}).count()>0){
#        print(it.user_name + " found in comments");
#    }
#    if (db.likes.find({user_id : follower}).count()>0){
#        print(it.user_name + " found in likes");
#    }
#});


#var follower_from_comments = 0;
#var follower_from_follows = 0;
#var follower_from_likes = 0;
#var hashtags = {};
#var comments = null;
#var likes = null;
#var follows = null;
#db.followers.find({active : true}).forEach( function(follower){
#    comments = db.comments.find({user_id : follower.user_id});
#    if (comments.count() > 0){
#        if (comments[0].tag in hashtags) {
#            hashtags[comments[0].tag] += 1;
#        } else {
#            hashtags[comments[0].tag] = 1;
#        }
#    }
#    follows = db.follows.find({user_id : follower.user_id});
#    if (follows.count() > 0){
#        if (follows[0].tag in hashtags) {
#            hashtags[follows[0].tag] += 1;
#        } else {
#            hashtags[follows[0].tag] = 1;
#        }
#    }
#    likes = db.likes.find({user_id : follower.user_id});
#    if (likes.count() > 0){
#        if (likes[0].tag in hashtags) {
#            hashtags[likes[0].tag] += 1;
#        } else {
#            hashtags[likes[0].tag] = 1;
#        }
#    }
#});
#var sortable = [];
#for (var item in hashtags) {
#    sortable.push([item, hashtags[item]]);
#}
#sortable.sort(function(a, b) {
#    return a[1] - b[1];
#});
#print(sortable);