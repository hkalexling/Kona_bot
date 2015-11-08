# Kona_bot
A twitter bot that post KonaChan images under my own Twitter account [@hkalexling](https://twitter.com/hkalexling) with tag `#KonaBot`

It's currently living on a VPS

### Main features
- Tweet a random image from [KonaChan](https://konachan.net) every X hours ( X can be changed by changing the variable `hourGap` in [kona_bot.py](https://github.com/hkalexling/Kona_bot/blob/master/kona_bot.py). The default vault is 2)
- Auto reply all Chinese mentions under tweets with `#KonaBot` tag ( powered by [SimSimi](http://developer.simsimi.com) )

### ToDo
- Auto reply direct messages

### Ackonwledgement
This bot used the following third party packages:
- [Twython](https://github.com/ryanmcgrath/twython)
- [Python_SimSimi](https://github.com/six519/python-simsimi)
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
