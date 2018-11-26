import numpy as np
import os
from skimage import io

def Read(filepath):
	base_path = filepath # '../../Untitled Folder/yalefaces_crop/'
	DataPath = []
	#print(os.listdir(base_path))
	for i in os.listdir(base_path):
	    if i != 'Readme.txt':
		DataPath.append(os.path.join(base_path, i))
		
		
	imData = []
	imLabels = []
	#print(DataPath)

	for file in DataPath:
	    #print('reading file')
	    imRead = io.imread(file, as_grey=True)
	    imData.append(imRead)
	    print(os.path.split(file)[1])
	    labelRead = int(os.path.split(file)[1].split("B")[1].split("_")[0]) #.replace("subject", "")) - 1 # Parse class label from file
	    print (labelRead)
	    imLabels.append(labelRead)
	return (imData, imLabels)

