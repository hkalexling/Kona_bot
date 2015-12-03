import requests
import random
from BeautifulSoup import BeautifulSoup

def generateNum():
	return str(random.randrange(1, 100000))

def downloadImg():
	rawurl = None
	bestScore = 0
	bestUrl = ''
	bestPostUrl = ''

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
			bestPostUrl = requestUrl

		rawurl = None

	print(bestUrl)
	print(bestScore)
	print(bestPostUrl)
	page = requests.get(bestUrl)
	with open('test.jpg', 'wb') as test:
 		test.write(page.content)
 		return bestPostUrl

