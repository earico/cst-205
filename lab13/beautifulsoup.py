from urllib.request import Request, urlopen
import numpy as np
import cv2
import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint

Url = 'https://www.google.com/'
open = urlopen(Url) #opening url

obj1 = BeautifulSoup(open, 'html.parser') #creating parser object
for link in obj1.findAll("img"): #for loop to find all img
    temp = link.get('src')
    if temp[:1] == "/":
        image = Url + temp #finding image and adding it to url for viewing
print(image) #printing image url

Img = urlopen(image) #open url

image2 = np.asarray(bytearray(Img.read()), dtype="uint8") #creating multidim array with vals of image
image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)

print(image2) #printing vals
