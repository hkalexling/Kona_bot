import requests
import random
from BeautifulSoup import BeautifulSoup

def generateNum():
	return str(random.randrange(1, 100000))

def downloadImg():
	rawurl = None
	bestScore = 0
	bestUrl = ''

	for i in range(0, 10):
		while rawurl is None: 
			num = generateNum()
			requestUrl = 'https://konachan.net/post/show/' + num
		 	page = requests.get(requestUrl)
			html = page.content
			parsed = BeautifulSoup(html)
			rawurl = parsed.body.find('div', attrs={'id':'note-container'})
			rawScore = parsed.body.find('span', attrs={'id':'post-score-' + num})

		url = rawurl.parent.find('img')['src']
		score = int(rawScore.text)

		if score > bestScore:
			bestScore = score
			bestUrl = url

		rawurl = None

	print(bestUrl)
	print(bestScore)
	page = requests.get(bestUrl)
	with open('Img/test.jpg', 'wb') as test:
 		test.write(page.content)
 		return requestUrl

