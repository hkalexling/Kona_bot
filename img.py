import requests
import random
from BeautifulSoup import BeautifulSoup

def generateNum():
	return str(random.randrange(1, 100000))

def downloadImg():
	rawurl = None
	while rawurl is None: 
	 	page = requests.get('https://konachan.com/post/show/' + generateNum())
		html = page.content
		parsed = BeautifulSoup(html)
		rawurl = parsed.body.find('div', attrs={'id':'note-container'})
	url = rawurl.parent.find('img')['src']
	print(url)
	page = requests.get(url)
	with open('Img/test.jpg', 'wb') as test:
 		test.write(page.content)

