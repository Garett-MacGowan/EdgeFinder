'''
Created on Sep 3, 2017

@author: Garett MacGowan
'''

#from moviepy.editor import *
from PIL import Image
from fractions import Fraction

def edgeFindImage(percentEdgeTolerance, imageLocation):
    original = Image.open(imageLocation)
    #original.show()
    newImageSize = original.size #Getting size of image as a tuple
    xDexMin = 0
    yDexMin = 0
    xDexMax = newImageSize[0]-1
    yDexMax = newImageSize[1]-1
    imageArray = original.load() #Loading original image into a readable/writable array format.
    
    grayImage = Image.new('L', newImageSize,) #Creating new gray scale type image, with empty color parameter so that we may occupy the color ourselves.
    grayImageArray = grayImage.load() #Loading the empty gray scale image into a readable/writable array format.
    
    #Performing gray scale conversion operations.
    for x in range(0,xDexMax):
        for y in range(0,yDexMax): #Scanning down each y on the x axis
            grayImageArray[x,y] = int((imageArray[x,y][0])*0.21 + (imageArray[x,y][1])*0.72 + (imageArray[x,y][2])*0.07)
    
    finalImage = Image.new('L', newImageSize,) #Creating new gray scale type image, with empty color parameter so that we may occupy the color ourselves.
    finalImageArray = finalImage.load() #Loading the empty gray scale type image into a readable/writable array format.
    
    edgeFindTolerance = (percentEdgeTolerance/100)*255

    #Populating finalImageArray with edges.
    for x in range(xDexMin,xDexMax):
        for y in range(yDexMin,yDexMax):
            currentLuminosity = grayImageArray[x,y]
            if (x == xDexMin):
                if (y == yDexMin):
                    if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    finalImageArray[x,y] = 255
                    continue
                if (y == yDexMax):
                    if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    finalImageArray[x,y] = 255
                    continue
                if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                finalImageArray[x,y] = 255
                continue
            if (y == yDexMin):
                if (x == xDexMax):
                    if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    finalImageArray[x,y] = 255
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                finalImageArray[x,y] = 255
                continue
            if (x == xDexMax):
                if (y == yDexMax):
                    if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                        finalImageArray[x,y] = 0
                        continue
                    finalImageArray[x,y] = 255
                    continue
                if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                finalImageArray[x,y] = 255
                continue
            if (y == yDexMax):
                if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                    finalImageArray[x,y] = 0
                    continue
                finalImageArray[x,y] = 255
                continue

            if (currentLuminosity > (grayImageArray[x-1,y-1] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x,y-1] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x+1,y-1] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x+1,y] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x+1,y+1] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x,y+1] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x-1,y+1] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            if (currentLuminosity > (grayImageArray[x-1,y] + edgeFindTolerance)):
                finalImageArray[x,y] = 0
                continue
            finalImageArray[x,y] = 255

    #Cleaning up island pixels from finalImageArray.
    for x in range(0,xDexMax):
        for y in range(0,yDexMax):
            #If the current pixel is black
            if (finalImageArray[x,y] == 0):
                if (x == xDexMin):
                    if (y == yDexMin):
                        if (finalImageArray[x+1,y] == 255 and finalImageArray[x+1,y+1] == 255 and finalImageArray[x,y+1] == 255):
                            finalImageArray[x,y] = 255
                        continue
                    if (y == yDexMax):
                        if (finalImageArray[x,y-1] == 255 and finalImageArray[x+1,y-1] == 255 and finalImageArray[x+1,y] == 255):
                            finalImageArray[x,y] = 255
                        continue
                    if (finalImageArray[x,y-1] == 255 and finalImageArray[x+1,y-1] == 255 and finalImageArray[x+1,y] == 255 and finalImageArray[x+1,y+1] == 255 and finalImageArray[x,y+1] == 255):
                        finalImageArray[x,y] = 255
                    continue
                if (y == yDexMin):
                    if (x == xDexMax):
                        if (finalImageArray[x-1,y] == 255 and finalImageArray[x-1,y+1] == 255 and finalImageArray[x,y+1] == 255):
                            finalImageArray[x,y] = 255
                        continue
                    if (finalImageArray[x-1,y] == 255 and finalImageArray[x-1,y+1] == 255 and finalImageArray[x,y+1] == 255 and finalImageArray[x+1,y+1] == 255 and finalImageArray[x+1,y] == 255):
                        finalImageArray[x,y] = 255
                    continue
                if (x == xDexMax):
                    if (y == yDexMax):
                        if (finalImageArray[x-1,y] == 255 and finalImageArray[x-1,y-1] == 255 and finalImageArray[x,y-1] == 255):
                            finalImageArray[x,y] = 255
                        continue
                    if (finalImageArray[x,y-1] == 255 and finalImageArray[x-1,y-1] == 255 and finalImageArray[x-1,y] == 255 and finalImageArray[x-1,y+1] == 255 and finalImageArray[x,y+1] == 255):
                        finalImageArray[x,y] = 255
                    continue
                if (y == yDexMax):
                    if (finalImageArray[x-1,y] == 255 and finalImageArray[x-1,y-1] == 255 and finalImageArray[x,y-1] == 255 and finalImageArray[x+1,y-1] == 255 and finalImageArray[x+1,y] == 255):
                        finalImageArray[x,y] = 255
                    continue
                else:
                    if (finalImageArray[x-1,y-1] == 255 and finalImageArray[x,y-1] == 255 and finalImageArray[x+1,y-1] == 255 and finalImageArray[x+1,y] == 255 and finalImageArray[x+1,y+1] == 255 and finalImageArray[x,y+1] == 255 and finalImageArray[x-1,y+1] == 255 and finalImageArray[x-1,y] == 255):
                        finalImageArray[x,y] = 255
    
    return finalImage

def main(percentEdgeTolerance, imageLocation, saveLocation, saveBoolean):
    imageEdges = edgeFindImage(percentEdgeTolerance, imageLocation)
    if (tesselateBoolean == 1):
        finalImage = tesselateImage(imageEdges)
    else:
        finalImage = imageEdges
    if (saveBoolean == 1):
        finalImage.save(saveLocation)
    finalImage.show()

edgeFindTolerance = 3.5
imageLocation = "D:/Downloads/test.jpg"
saveLocation = "D:/Downloads/tester.png"
saveBoolean = 0

main(edgeFindTolerance, imageLocation, saveLocation, saveBoolean)
