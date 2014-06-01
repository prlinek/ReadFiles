__author__ = 'VM_PRL'

import numpy
import csv
import glob
import os
#import sys

datapath = '../DataPack1'
filemask = 'scan_down_'

if not os.path.isdir(datapath):
    print "Entered Data path does not exist!"

# rows = []
x = []


# reading data file
def readFile(fname):
    global rows  # test
    rows = []
    f = open(fname, 'rb')
    reader = csv.reader(f, delimiter='\t')
    for n, row in enumerate(reader):
        if len(rows) < n+1:
            rows.append([])
            rows[n].extend(row)
    f.close()
    return rows


# reading batches of files
def readFiles():
    if os.path.isdir(datapath):
        print "processing a directory"
        list_of_files = glob.glob('%s/%s*' % (datapath, filemask))
        list_of_files.sort()  # need to sort it in different way!
        print "Number of files in directory: %d \n" % len(list_of_files)
    else:
        print "processing a list of files"
        #list_of_files = sys.argv[1:]

    # y = numpy.array([])
    for file_name in list_of_files:
        print file_name
        readFile(file_name)
        data = numpy.array(rows, float)
        x.append(data)
        # print data

    return x

# readFile(datapath + '/scan_down_0')
# x = numpy.array(rows, float)
# readFile(datapath + '/scan_down_1')
# y = numpy.array(rows, float)
# print x + y
readFiles()
print x[189], "\n"
y = x[1]
print y[1, 1]
