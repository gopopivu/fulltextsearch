import urllib
from bs4 import BeautifulSoup
import re

class Parser:
  def __init__(self, html):
    self.html = html

  def get_text_from_html(self):
    soup = BeautifulSoup(self.html)
    for script in soup(["script", "style"]):
      script.extract()
    return ' '.join(self.normilize(soup.get_text()))

  def normilize(self, text):
    pattern = re.compile('[\W_]+')
    text = pattern.sub(' ', text)
    words = text.split()
    from nltk.corpus import stopwords
    words = [word.lower() for word in words if word not in stopwords.words("english")]
    from stemming.porter2 import stem
    stemmed_words = [stem(word) for word in words]
    return stemmed_words