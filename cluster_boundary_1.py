import os
import csv
import numpy as np

os.chdir('/Maroof/python/personal_proj/cluster_boundary/')
file = open('circle_data_points.csv')
fileRead = csv.reader(file)
fileData = list(fileRead)

arr = []
for line in fileData:
    try:
        arr.append(float(line[0]))
    except ValueError:
        pass

print(np.max(arr), np.min(arr))
