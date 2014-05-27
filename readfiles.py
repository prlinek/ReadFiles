__author__ = 'VM_PRL'

import numpy
import csv
import glob
import os
#import sys

datapath = './DataPack1'
filemask = 'scan_down_'

if not os.path.isdir(datapath):
    print "Entered Data path does not exist!"

rows = []
x = []
# y = numpy.array([])

# reading data file
def readFile(fname):
    f = open(fname, 'rb')
    reader = csv.reader(f, delimiter='\t')
    for n, row in enumerate(reader):
        if len(rows) < n+1:
            rows.append([])
            rows[n].extend(row)
    f.close()

# reading batches of files
def readFiles():
    if os.path.isdir(datapath):
        print "processing a directory"
        list_of_files = glob.glob('%s/%s*' % (datapath, filemask))
        list_of_files.sort()  # need to sort it in different way!
    else:
        print "processing a list of files"
        #list_of_files = sys.argv[1:]

    # i = 0
    y = numpy.array([])
    for file_name in list_of_files:
        print file_name
        readFile(file_name)
        data = numpy.array(rows, float)
        print data
        # y = numpy.append(y, data, )
        # x.append(data)
        # x[i].extend(data)
        # i += 1

    print y

readFiles()
