import bottle, pymongo
from models.followers_tags_model import FollowersTagsModel
from models.followers_model import FollowersModel

followers_tags_model = FollowersTagsModel()
followers_model = FollowersModel()

@bottle.get('/<filename:re:.*\.css>')
@bottle.get('/<filename:re:.*\.js>')
def send_static(filename):
    return bottle.static_file(filename, root='node_modules/')

@bottle.route('/dashboard')
def index():
    date = followers_model.getFirstDate()
    best_tags = followers_tags_model.getBestTags(date)
    worst_tags = followers_tags_model.getWorstTags(date)
    followers_growth = followers_model.getGrowth(date)
    return bottle.template("dashboard", best_tags=best_tags, worst_tags=worst_tags, followers_growth=followers_growth)
bottle.run(host='0.0.0.0', port=8080)
