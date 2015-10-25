from twython import Twython
import random
import threading

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')
time = 5000

def prepare():
	if random.random() < 1/time:
		post()
	threading.Timer(1, prepare).start()

def post():
	txtList = open('randomText.txt').read().split(';')
	text = txtList[random.randrange(0, len(txtList))]
	finalText = '#KonaBot ' + text.replace('\n', '')
	print finalText
	twitter.update_status(status=finalText)

prepare()
