from twython import Twython
from img import downloadImg
import threading

time = 3600

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

def post():
	downloadImg()

	photo = open('Img/test.jpg', 'rb')
	response = twitter.upload_media(media=photo)
	twitter.update_status(status='#KonaBot', media_ids=[response['media_id']])
	threading.Timer(time, post).start()

post()
