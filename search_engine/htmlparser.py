import urllib
from bs4 import BeautifulSoup
import re
import copy

def delete_marks(text):
  pattern = re.compile('[\W_]+')
  return pattern.sub(' ', text)

class Parser:
  def __init__(self, html):
    self.html = html

  def get_text_from_html(self):
    soup = BeautifulSoup(self.html)
    for script in soup(["script", "style"]):
      script.extract()
    return soup.get_text()

  def get_normalized_html(self):
    soup = BeautifulSoup(self.html)
    soup = self.get_text_from_html()
    return ' '.join(self.normalize(soup))

  def get_title(self):
    soup = BeautifulSoup(self.html)
    return soup.title.contents[0]

  def normalize(self, text):
    delete_marks(text)
    words = text.split()
    from nltk.corpus import stopwords
    words = [word.lower() for word in words if word not in stopwords.words("english")]
    from stemming.porter2 import stem
    stemmed_words = [stem(word) for word in words]
    return stemmed_words