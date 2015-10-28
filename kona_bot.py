from twython import Twython
from img import downloadImg
from datetime import datetime
import threading

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

def post():
	downloadImg()

	photo = open('Img/test.jpg', 'rb')
	response = twitter.upload_media(media=photo)
	twitter.update_status(status='#KonaBot', media_ids=[response['media_id']])

def checkTime():
	while True:
		now = datetime.now()
		if now.minute == 0 and now.second == 0:
			post()
			return

def main():
	now = datetime.now()
	if now.minute == 59:
		checkTime()
	threading.Timer(30, main).start()

main()



