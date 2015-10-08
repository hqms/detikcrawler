from bs4 import BeautifulSoup
import requests

__author__ = 'hakim'


print 'Fetch content from detikcom'
r = requests.get('http://www.detik.com')

soup  = BeautifulSoup(r.content, 'html.parser')

imgs = soup.find_all('img')
print 'Total img tags ', imgs.__len__()
# for i in imgs:
#     print i