from InstagramAPI import InstagramAPI
from datetime import datetime
import constantRaspbian
import sys
sys.path.insert(0, '/home/pi/develop/instabot.py/instabot_py/models')
from medias_model import MediasModel

medias_model = MediasModel();

InstagramAPI = InstagramAPI(constantRaspbian.LOGIN, constantRaspbian.PASS)
InstagramAPI.login()

InstagramAPI.getSelfUserFeed()
medias =  InstagramAPI.LastJson
total_added = 0
for item in medias['items']:
    total_added += medias_model.save(item, datetime.now())
    InstagramAPI.getMediaLikers(item['id'])
    likers = InstagramAPI.LastJson
    medias_model.saveLikers(item['id'], likers, datetime.now())
