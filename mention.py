#coding:utf-8
from twython import Twython
from twython import TwythonStreamer
from simsimi import chat
import sys  
import threading

reload(sys)  
sys.setdefaultencoding('utf8')

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

def handleStatus(input_id):
	dict = twitter.show_status(id = input_id)
	k = dict.keys()
	v = dict.values()

	for n in range(0, len(k)):
		if k[n] == 'text':
			if '#KonaBot' in v[n]:
				return True

	return False

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
    	if 'in_reply_to_status_id_str' in data:
    		if data['in_reply_to_status_id_str'] != None:
    			if handleStatus(data['in_reply_to_status_id_str']):
    				tweet_id = data['id']
    				if 'user' in data:
    					if data['user']['screen_name'] != 'hkalexling':
	    					user = '@' + data['user']['screen_name'] + ' '
	    					text = data['text'].replace(data['text'].split(' ')[0], '')
		    				string = '#KonaBot自动回复 ' + user + chat(text)
		    				print str(string)
		    				twitter.update_status(status=string, in_reply_to_status_id = tweet_id)
    def on_error(self, status_code, data):
        print status_code, data

stream = MyStreamer('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

stream.user()
