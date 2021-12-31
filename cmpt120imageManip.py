# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Julianne Chiu, Kirby Rodriguez
# Date: December 5, 2020
# Description:

import cmpt120imageProj
import numpy

#Basic Functions

#invert subtracts the RNG values from 255 to get their inverted values
def invert(img):
  for i in range(len(img)):
    for j in range(len(img[0])):
      pixel = img[i][j]
      newpixel = []
      flipR = 255 - int(pixel[0])
      flipG = 255 - int(pixel[1])
      flipB = 255 - int(pixel[2])
      newpixel.append(flipR)
      newpixel.append(flipG)
      newpixel.append(flipB)
      img[i][j] = newpixel
  return img

#fliph flips the image horizentally by moving pixel columns to the opposite side of the image
def fliph(img):
     newimg = cmpt120imageProj.getImage("project-photo.jpg")
     for i in range(len(img)):
         for j in range(len(img[0])):
             newimg[i][j] = img[len(img)-i-1][j]
     return newimg

#flipv flips the image vertically by moving pixel rows to the opposite side of the image
def flipv(img):
     newimg = cmpt120imageProj.getImage("project-photo.jpg")
     for i in range(len(img)):
         for j in range(len(img[0])):
             newimg[i][j] = img[i][(len(img[0])-j-1)]
     return newimg

#Intermediate functions

#removered sets the red value in the RGB to 0
def removered(img):
     for i in range(len(img)):
         for j in range(len(img[0])):
             pixel = img[i][j]
             pixel[0] = 0
     return img

#removegreen sets the green value in the RGB to 0
def removegreen(img):
     for i in range(len(img)):
         for j in range(len(img[0])):
             pixel = img[i][j]
             pixel[1] = 0
     return img

#removeblue sets the blue value in the RGB to 0
def removeblue(img):
     for i in range(len(img)):
         for j in range(len(img[0])):
             pixel = img[i][j]
             pixel[2] = 0
     return img

#grayscale takes the average of the RGB numbers and sets each value to that average
def grayscale(img):
     for i in range(len(img)):
         for j in range(len(img[0])):
             pixel = img[i][j]
             average = (pixel[0] + pixel[1] + pixel[2]) / 3
             pixel[0] = average
             pixel[1] = average
             pixel[2] = average
     return img

#sepia uses the formula for finding the value of sepiared, sepiagreen, and sepiablue, and sets the RGB values to those numbers
def sepia(img):
  for i in range(len(img)):
    for j in range(len(img[0])):
      pixel = img[i][j]
      sepiaRed = int(pixel[0] * 0.393) + int(pixel[1] * 0.769) + int(pixel[2] * 0.189)
      if sepiaRed > 255:
          sepiaRed = 255
      sepiaGreen = int(pixel[0] * 0.349) + int(pixel[1] * 0.686) + int(pixel[2] * 0.168)
      if sepiaGreen > 255:
          sepiaGreen = 255
      sepiaBlue = int(pixel[0] * 0.272) + int(pixel[1] * 0.534) + int(pixel[2] * 0.131)
      if sepiaBlue > 255:
          sepiaBlue = 255
      pixel[0] = sepiaRed
      pixel[1] = sepiaGreen
      pixel[2] = sepiaBlue
  return img

#dbrightness decreases the image's brightness by subtracting 10 from each RGB channel
def dbrightness(img):
     for i in range(len(img)):
         for j in range(len(img[0])):
             pixel = img[i][j]
             pixel[0] = pixel[0] - 10
             if pixel[0] < 0:
                 pixel[0] = 0
             pixel[1] = pixel[1] - 10
             if pixel[1] < 0:
                 pixel[1] = 0
             pixel[2] = pixel[2] - 10
             if pixel[2] < 0:
                 pixel[2] = 0
     return img

#ibrightness increases the image's brightness by adding 10 to each RGB channel
def ibrightness(img):
     for i in range(len(img)):
         for j in range(len(img[0])):
             pixel = img[i][j]
             pixel[0] = pixel[0] + 10
             if pixel[0] > 255:
                 pixel[0] = 255
             pixel[1] = pixel[1] + 10
             if pixel[1] > 255:
                 pixel[1] = 255
             pixel[2] = pixel[2] + 10
             if pixel[2] > 255:
                 pixel[2] = 255

     return img

#Advanced functions

#rotateleft rotates the image 90 degrees anti-clockwise by reversing the image list and then pairing the first elements of every list together
def rotateleft(img):
     img = list(zip(*img[::-1]))
     return img

#rotateright rotates the image 90 degrees clockwise by pairing the first elements of every list together and then reversing that list
def rotateright(img):
     img = list(reversed(list(zip(*img))))
     return img

#pixelate gets the average rgb values in a 4x4 section and sets new values based on the RGB channels in that section
def pixelate(img):
     redTotal = 0
     greenTotal = 0
     blueTotal = 0
     height = len(img[0]) - len(img[0])%4
     width = len(img) - len(img)%4

     for y in range(0, height, 4):
         for x in range(0, width, 4):
             for a in range(4):
                 for b in range(4):
                     redTotal += img[x+a][y+b][0]
                     greenTotal += img[x+a][y+b][1]
                     blueTotal += img[x+a][y+b][2]
             for a in range(4):
                 for b in range(4):
                     img[x+a][y+b][0] = int(redTotal/16)
                     img[x+a][y+b][1] = int(greenTotal/16)
                     img[x+a][y+b][2] = int(blueTotal/16)
             redTotal = 0
             greenTotal = 0
             blueTotal = 0

     return img

#binarize uses the algorithm for finding threshold values and compares each pixels average RGB value to determine whether it turns black or white
def binarize(img):
     grayscale(img)
     threshold = 0

     for i in img:
         for j in i:
             threshold += j[0]
     threshold = int(threshold/(len(img) * len(img[0])))
     new_col = []
     beforeThreshold = []
     afterThreshold = []

     for num in range(len(img[0])):
         new_col += [[0,0,0]]

     for num in range(len(img)):
         beforeThreshold += [new_col[:]]
         afterThreshold += [new_col[:]]

     wrongThreshold = True
     while wrongThreshold:
         for i in range(len(img)):
             for j in range(len(img[0])):
                 if img[i][j][0] <= threshold:
                     beforeThreshold[i][j] = img[i][j]
                 else:
                     afterThreshold[i][j] = img[i][j]

         avg1 = 0
         for i in beforeThreshold:
             for j in i:
                 avg1 += j[0]
         avg1 = avg1/(len(img) * len(img[0]))

         avg2 = 0
         for i in afterThreshold:
             for j in i:
                 avg2 += j[0]
         avg2 = avg2/(len(img)*len(img[0]))
         newThreshold = int((avg2 + avg1)/2)

         if threshold - newThreshold <= 10:
             wrongThreshold = False
         else:
             threshold = newThreshold

     for m in range(len(img)):
         for n in range(len(img[0])):
             pixel = img[m][n]
             if pixel[0] <= newThreshold:
                 pixel[0] = 0
                 pixel[1] = 0
                 pixel[2] = 0
             elif pixel[0] >= newThreshold:
                 pixel[0] = 255
                 pixel[1] = 255
                 pixel[2] = 255
     return img




