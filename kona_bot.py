from twython import Twython
from img import downloadImg
from datetime import datetime
import threading

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')
hourGap = 2 #Tweet every two hours
nextPostTime = None

def post():
	url = downloadImg()

	photo = open('Img/test.jpg', 'rb')
	response = twitter.upload_media(media=photo)
	try:
		twitter.update_status(status='#KonaBot ' + url + ' ', media_ids=[response['media_id']])
	except Exception:
		pass

def checkTime():
	while True:
		now = datetime.now()
		if now.minute == 0 and now.second == 0:
			if nextPostTime == None or nextPostTime == now.hour:
				nextPostTime = now.hour
				nextPostTime += hourGap
				if nextPostTime > 24:
					nextPostTime -= 24
				post()
				return

def main():
	now = datetime.now()
	if now.minute == 59:
		checkTime()
	threading.Timer(30, main).start()

main()



