from urllib.request import Request, urlopen
import numpy as np
import cv2
import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint

Url = 'https://www.google.com/'
open = urlopen(Url)

obj1 = BeautifulSoup(open, 'html.parser')
for link in obj1.findAll("img"):
    temp = link.get('src')
    if temp[:1] == "/":
        image = Url + temp
print(image)

Img = urlopen(image)

image2 = np.asarray(bytearray(Img.read()), dtype="uint8")
image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)

print(image2)
'''
Url = 'https://hsreplay.net/archetypes/223/odd-warrior?hl=en'

req = Request( Url, headers={'User-Agent': 'Mozilla/5.0'} )
res = urlopen(req)
object1 = BeautifulSoup(res.read(), 'lxml')
title = object1.body.h1

print(title.get_text())
for link in object1.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

object2 = BeautifulSoup(res.read(), 'lxml')

for link in object2.findAll("img"):
    temp = link.get('src')
    image = Url + temp
print(image)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

res = requests.get('http://google.com').text
soup = BeautifulSoup(res,"lxml")
for item in soup.select(".article-image"):
    print(urljoin('http://google.com',item['src']))
'''
