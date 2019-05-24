from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication, QPushButton,QVBoxLayout,QMainWindow, QLineEdit)
import sys
from PyQt5.QtCore import pyqtSlot, QUrl, Qt

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon

import glob

from PIL import Image

#provided dictionary which will be used to

image_info = [
            {
                "id" : "34694102243_3370955cf9_z",
                "title" : "Eastern",
                "flickr_user" : "Sean Davis",
                "tags" : ["Los Angeles", "California", "building"]
                      },
            {
                "id" : "37198655640_b64940bd52_z",
                "title" : "Spreetunnel",
                "flickr_user" : "Jens-Olaf Walter",
                "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
                      },
            {
                "id" : "36909037971_884bd535b1_z",
                "title" : "East Side Gallery",
                "flickr_user" : "Pieter van der Velden",
                "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
                      },
            {
                "id" : "36604481574_c9f5817172_z",
                "title" : "Lombardia, september 2017",
                "flickr_user" : "Mónica Pinheiro",
                "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
                      },
            {
                "id" : "36885467710_124f3d1e5d_z",
                "title" : "Palazzo Madama",
                "flickr_user" : "Kevin Kimtis",
                "tags" : [ "Rome", "Italy", "window", "road", "building"]
                      },
            {
                "id" : "37246779151_f26641d17f_z",
                "title" : "Rijksmuseum library",
                "flickr_user" : "John Keogh",
                "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
                      },
            {
                "id" : "36523127054_763afc5ed0_z",
                "title" : "Canoeing in Amsterdam",
                "flickr_user" : "bdodane",
                "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
                      },
            {
                "id" : "35889114281_85553fed76_z",
                "title" : "Quiet at dawn, Cabo San Lucas",
                "flickr_user" : "Erin Johnson",
                "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
                      },
            {
                "id" : "36140096743_df8ef41874_z",
                "title" : "Someday",
                "flickr_user" : "Thomas Hawk",
                "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
                      },
            {
                "id" : "34944112220_de5c2684e7_z",
                "title" : "View from our rental",
                "flickr_user" : "Doug Finney",
                "tags" : ["Mexico", "ocean", "beach", "palm"]
                      }
            ]

#Places all the images from the folder into a usable dictionary
img = glob.glob("hw3-images/images/*.jpg")
imageDict=[]
for i in img:
   imageDict.append(Image.open(i))

   #Creates the GUI widget
class Log(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()


   def initUI(self):

       #Creates the widget box template
       self.input = QLineEdit()
       self.combo = QComboBox()
       self.lbl1 = QLabel("Input below",self)
       self.button = QPushButton("Search")


       #Creates a drop down menu which a imgage filter will be seleceted
       self.button.clicked.connect(self.comboActivated)

       #List of image filters which can be seleceted
       self.combo.addItem("sepia")
       self.combo.addItem("negative")
       self.combo.addItem("grayscale")
       self.combo.addItem("thumbnail")
       self.combo.addItem("none")

       vbox = QVBoxLayout()

       #Adds an input box to the widget and a button
       vbox.addWidget(self.lbl1)
       vbox.addWidget(self.input)
       vbox.addWidget(self.combo)
       vbox.addWidget(self.button)

       self.setLayout(vbox)
       self.setWindowTitle("Image Seach")

       self.show()

       """
		#CREDIT

           **** Provided by my classmate Jonathan Quintero ****


       """
   def comboActivated(self):
       text = self.combo.currentText()
       print(text)

       #Points system allows for the highest number to be returned
       #which will be the index value for the image with the most tag matches

       points = [0,0,0,0,0,0,0,0,0,0]
       #Loop that oders the images through incrementing an interger array
       #by how many tags are found in the searched pharse
       for i in range(len(image_info)):
           if(image_info[i]["title"] == self.input.text()):
               points[i] += 100
           for z in range(len(image_info[i]["tags"])):
               if image_info[i]["tags"][z] in self.input.text(): #Checks if a tag if found within the searched phrase
                   points[i] += 1

       #Returns the highest value within the asarray
       #which represents the image with the most tag "hits"
       picker = max(points)
       thisOne = 0
       for i in range(len(points)):
           if(points[i]==picker):
               thisOne=i
               break
       if picker == 0:
           print("ooof, try again")
       else:
           self.chooserChange(text,thisOne)


   #Fucntion which compares if the slected was chosen
   #then proceeds to call the Fucntion fot the filter
   def chooserChange(self, text, num):
       if(text=="none"):
           self.noneChange(num)
       if(text=="sepia"):
           self.sepiaChange(num)
       if(text=="negative"):
           self.negativeChange(num)
       if(text=="grayscale"):
           self.grayscaleChange(num)
       if(text=="thumbnail"):
           self.thumbnailChange(num)

   #Halves the size of the image
   def thumbnailChange(self,num):
       im = imageDict[num]
       mi = Image.new("RGB", (int(im.width/2), int(im.height/2)))
       for x in range(int(im.width/2)):
           for y in range(int(im.height/2)):
                   red,green,blue = im.getpixel((x,y))
                   newcolor=((red),
                           (green),
                           (blue))
                   mi.putpixel((x,y), newcolor)
       mi.show()

   #Grayscales the image
   def grayscaleChange(self,num):
       im = imageDict[num]
       mi = Image.new("RGB", (im.width, im.height))
       for x in range(im.width):
           for y in range(im.height):
               red,green,blue = im.getpixel((x,y))
               rgbMono = int((red+green+blue)/3)
               newcolor = ((rgbMono),
                           (rgbMono),
                           (rgbMono))
               mi.putpixel((x,y), newcolor)
       mi.show()

   #Negative filter takes the original image's pixel values and then subtracts
   def negativeChange(self,num):
       im = imageDict[num]
       mi = Image.new("RGB", (im.width, im.height))
       for x in range(im.width):
           for y in range(im.height):
               red,green,blue = im.getpixel((x,y))
               newcolor = (int(255-red),
                           int(255-green),
                           int(255-blue))
               mi.putpixel((x,y), newcolor)
       mi.show()


   #Changes every pixels tuples to corresponding values that
   #relates that of a sepia image filter
   def sepiaChange(self,num):
       im = imageDict[num]
       mi = Image.new("RGB", (im.width,im.height))
       for x in range(im.width):
           for y in range(im.height):
               red,green,blue = im.getpixel((x,y))
               newcolor = (int(red *.5),
                           int(green *.3),
                           int(blue *.1))
               mi.putpixel((x,y), newcolor)
       mi.show()

   #Displays the image without a filter applied on it
   def noneChange(self,num):
       #print(num)
       im = imageDict[num]
       im.show()

#Calls the class to be activated
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Log()
   sys.exit(app.exec_())

