#coding:utf-8
from twython import Twython
import sys  
import threading

reload(sys)  
sys.setdefaultencoding('utf8')
time = 10

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

def mention():
	getMention()
	threading.Timer(time, mention).start()

def getMention():
	for i in twitter.get_mentions_timeline():
		shouldReply = False
		tweet_id = ''
		user = 'whoever'

		k = i.keys()
		v = i.values()
		for n in range(0, len(k)):
			if k[n] == 'user':
				user = handleUser(v[n])
			
			if k[n] == 'id':
				tweet_id = v[n]
			
			if k[n] == 'in_reply_to_status_id_str':
				repliedFile = open('replied_id.txt', 'rb')
				if str(tweet_id) in repliedFile.read():
					return
				shouldReply = handleStatus(v[n])
			
		if shouldReply:
			if user != 'whoever':
				string = '#KonaBot' + user + '乃找我主人有事吗~'
				twitter.update_status(status=string, in_reply_to_status_id = tweet_id)
				with open('replied_id.txt', 'wb') as repliedFile:
					repliedFile.write(str(tweet_id))
			print 'replied'

		return

			
def handleUser(input):
	k = input.keys()
	v = input.values()
	for n in range(0, len(k)):
		if k[n] == 'screen_name':
			return ' @' + v[n] + ' '

	return 'whoever'

def handleStatus(input_id):
	dict = twitter.show_status(id = input_id)
	k = dict.keys()
	v = dict.values()

	for n in range(0, len(k)):
		if k[n] == 'text':
			if '#KonaBot' in v[n]:
				print v[n]
				return True

	return False

mention()