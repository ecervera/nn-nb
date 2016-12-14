# The German Traffic Sign Recognition Benchmark
#
# sample code for reading the traffic sign images and the
# corresponding annotation data
#
# have fun, Christian

import matplotlib.pyplot as plt
import csv

# function for reading the images
# arguments: path to the traffic sign data, for example './GTSRB/Training'
# returns: list of images, lists of corresponding dimensions, ROIs, and labels 
def readTrafficSigns(rootpath, classes, tracks):
    '''Reads traffic sign data for German Traffic Sign Recognition Benchmark.
    Arguments: path to the traffic sign data, for example './GTSRB/Training'
               list of classes to be loaded
               dictionary of tracks for each class
    Returns:   list of images, list of corresponding dimensions, ROIs, 
               labels, and filenames'''

    images = [] # images
    dims = []
    ROIs = []
    labels = [] # corresponding labels
    filenames = []
    # loop over the selected classes and tracks
    for c in classes:
        prefix = rootpath + '/' + format(c, '05d') + '/' # subdirectory for class
        gtFile = open(prefix + 'GT-'+ format(c, '05d') + '.csv') # annotations file
        gtReader = csv.reader(gtFile, delimiter=';') # csv parser for annotations file
        gtReader.next() # skip header
        # loop over all images in current annotations file
        for row in gtReader:
            filename = row[0]
            if tracks[c]== int(filename[0:5]):
                images.append(plt.imread(prefix + filename)) # the 1th column is the filename
                dims.append((int(row[1]),int(row[2])))
                ROIs.append(((int(row[3]),int(row[4])),(int(row[5]),int(row[6]))))
                labels.append(row[7]) # the 8th column is the label
                filenames.append(filename)
        gtFile.close()
    return images, dims, ROIs, labels, filenames
