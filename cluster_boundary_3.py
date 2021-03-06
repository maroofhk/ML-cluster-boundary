import os
import csv
import numpy as np
import math

from matplotlib import pyplot as plt

def starter():
    os.chdir('/Maroof/python/personal_proj/cluster_boundary/')
    file = open('circle_data_points.csv')
    fileRead = csv.reader(file)
    fileData = list(fileRead)

    file.close()

    return fileData

def findMinMax(arrayFromFile):
    arrX = []
    arrY = []

    listOfExtrema = []
    
    for ind, item in enumerate(arrayFromFile):
        try:
            arrX.append(float(item[0]))
        except ValueError:
            pass

    for ind, item in enumerate(arrayFromFile):
        try:
            arrY.append(float(item[1]))
        except ValueError:
            pass

    listOfExtrema.append(arrX.index(np.max(arrX)))
    listOfExtrema.append(arrX.index(np.min(arrX)))
    listOfExtrema.append(arrY.index(np.max(arrY)))
    listOfExtrema.append(arrY.index(np.min(arrY)))

    return listOfExtrema

def rotatedCoordinates(arrayFromFile,theta):
    rotationMatrix = [[math.cos(math.radians(theta)),math.sin(math.radians(theta))],
                      [-1*math.sin(math.radians(theta)),math.cos(math.radians(theta))]]
    rotatedCoord = []
    #arrayFromFile = arrayFromFile[1:]
    for coord in arrayFromFile:
        x_prime = round((rotationMatrix[0][0])*float(coord[0])+(rotationMatrix[0][1])*float(coord[1]),2)
        y_prime = round((rotationMatrix[1][0])*float(coord[0])+(rotationMatrix[1][1])*float(coord[1]),2)
        rotatedCoord.append([x_prime,y_prime])
    return rotatedCoord

def listMinMaxIndice(arrayFromFile,listOfAngles):
    overallListIndices = []
    for theta in listOfAngles:
        rotateCoord = rotatedCoordinates(arrayFromFile, theta)
        listOfIndices = findMinMax(rotateCoord)
        for element in listOfIndices:
            if element not in overallListIndices:
                overallListIndices.append(element)

    listCoord = [arrayFromFile[element] for element in overallListIndices]
    return listCoord

def unzipCoordinates(arrayFromFile):
    x,y = zip(*arrayFromFile)
    x,y = list(x),list(y)
    x_val, y_val = [float(element) for element in x],[float(element) for element in y]
    return x_val, y_val

def scatterPlot(x,y,xBoundary,yBoundary):
    plt.scatter(x,y, color='b')
    plt.scatter(xBoundary,yBoundary, color='r')
    plt.show()

if __name__ == '__main__':
    #--- fully functional system
    
    arrayFromFile = starter()
    listAngles = [0,45]
    listCoord = listMinMaxIndice(arrayFromFile[1:], listAngles)
    x,y = unzipCoordinates(arrayFromFile[1:])
    xBoundary, yBoundary = unzipCoordinates(listCoord)
    scatterPlot(x,y,xBoundary,yBoundary)
    

