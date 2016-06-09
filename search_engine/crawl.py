import urllib
from bs4 import BeautifulSoup

class Crawler:
 	def __init__(self, urlbase, max_depth = 3, max_length = 10):
 		self.urlbase = urlbase
 		self.max_depth = max_depth
 		self.max_length = max_length
 		self.depth = 0
 		self.length = 0
 		self.urls = [urlbase]
 		self.was_here = [urlbase]

 	def crawl(self, url):
 		self.was_here.append(url)
 		local_urls = []
 		html = urllib.urlopen(url).read()
 		soup = BeautifulSoup(html)
		for link in soup.findAll('a'):
			href = link.get('href')
  	 		if href and href.startswith('/'):
  	 			print [e for e in href.split('/') if e]
  	 			if len([e for e in href.split('/') if e]) == self.depth + 1:
  	 				local_urls.append(self.urlbase + href)
  	 	print local_urls
  	 	for an_url in local_urls:
  	 			if an_url not in self.was_here:
		 			self.depth += 1
		 			self.length += 1
		 			if self.depth < self.max_depth or self.length < self.max_length:
		 				print an_url
		 				self.urls.append(an_url)
		 				self.crawl(an_url)
		 			else:
		 				break

	def get_links(self):
		self.crawl(self.urlbase)
		return self.urls

if __name__ == '__main__':
	s = Crawler('http://bbc.com')
	print s.get_links()


