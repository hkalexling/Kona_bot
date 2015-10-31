#coding:utf-8
from twython import Twython
from twython import TwythonStreamer
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

twitter = Twython('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
    	if 'user' in data:
    		userName = data['user']['screen_name']
    		favoriteList = open('favoriteList.txt').read().split(';')
    		if userName in favoriteList:
    			id = data['id']
    			try:
    			    twitter.create_favorite(id = id)
    			except Exception:
    			    pass
    	
    def on_error(self, status_code, data):
        print status_code, data

stream = MyStreamer('Consumer Key', 'Consumer Secret', 'Access Token', 'Access Token Secret')

stream.user()
