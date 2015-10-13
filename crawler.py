from _socket import timeout
from bs4 import BeautifulSoup
from pip._vendor.requests.exceptions import ReadTimeout
import requests
from setuptools.sandbox import ExceptionSaver

__author__ = 'hakim'


print 'Fetch content from detikcom'
r = requests.get('http://www.detik.com')

soup  = BeautifulSoup(r.content, 'html.parser')

imgs = soup.find_all('img')
print 'Total img tags ', imgs.__len__()
all_images = []
total_images_size = 0
for i in imgs:

    src = i['src']
    if src[0:7] == 'http://' or src[0:8] == 'https://':
        prefix = ''
    elif src[0:2] == '//':
        prefix = 'http:'
    else:
        prefix = 'http://www.detik.com/'

    img = prefix+i['src']
    try:
        r = requests.get(img, params=None, timeout=3, verify=True)
        if r.headers['content-type'][0:5] == 'image':
            all_images.append({'image': img, 'size': r.headers['content-length']})
            total_images_size += int(r.headers['content-length'])

    except ReadTimeout as e:
        all_images.append({'image': img, 'size': 0, 'status': 'timeout'})
    except Exception as e:
        all_images.append({'image': img, 'size': 0, 'status': e.message})


print "All images size %d bytes " % total_images_size
print all_images