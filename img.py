import requests
import random
from BeautifulSoup import BeautifulSoup

def generateNum():
	return str(random.randrange(1, 100000))

def downloadImg():
	rawurl = None
	while rawurl is None: 
		requestUrl = 'https://konachan.net/post/show/' + generateNum()
		#Use 'https://konachan.com if you don't mind the bot posting some sexual or offensive images.
	 	page = requests.get(requestUrl)
		html = page.content
		parsed = BeautifulSoup(html)
		rawurl = parsed.body.find('div', attrs={'id':'note-container'})
	url = rawurl.parent.find('img')['src']
	print(url)
	page = requests.get(url)
	with open('Img/test.jpg', 'wb') as test:
 		test.write(page.content)
 		return requestUrl

