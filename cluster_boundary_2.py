import os
import csv
import numpy as np

def starter():
    os.chdir('/Maroof/python/personal_proj/cluster_boundary/')
    file = open('circle_data_points.csv')
    fileRead = csv.reader(file)
    fileData = list(fileRead)

    return fileData

def findMinMax(arrayFromFile):
    index = []
    arr = []
    for ind, item in enumerate(arrayFromFile):
        try:
            arr.append(float(item[0]))
            index.append(ind)
        except ValueError:
            pass

    print('max: ',np.max(arr),', min: ', np.min(arr))
    print('index of max',arr.index(np.max(arr)),', index of min: ', arr.index(np.min(arr)))

def rotationMatrix(coord,angle):
    matrix = [[]]

if __name__ == '__main__':
    arrayFromFile = starter()
    findMinMax(arrayFromFile)
