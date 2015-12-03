from twython import Twython
from img import downloadImg
import time

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')
hourGap = 2 #Tweet every two hours
nextPostTime = None

def post():
	url, postUrl = downloadImg()

	try:
		twitter.update_status(status='#KonaBot ' + postUrl + ' ' + url)
	except Exception:
		pass


def main():
	period = hourGap * 3600
	while True:
		leftSecs = period - time.time() % period
		time.sleep(leftSecs)
		post()

main()



