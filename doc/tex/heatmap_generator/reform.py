#! /usr/bin/env python3
import numpy
import re
import sys

args = sys.argv
arr_size =int(args[1])
readfile = args[2]
writefile = args[3]


arr = numpy.zeros((arr_size, arr_size)).tolist()
regex0 = re.compile('\(\([-+]?[0-9]*\.?[0-9]+, [-+]?[0-9]*\.?[0-9]+\)\, ')
regex1 = re.compile('[^0-9 ]')

file0 = open(readfile, 'r')
file1 = open(writefile, 'w+')
for x in range(0, arr_size):
    for y in range(0, arr_size):
        string = file0.readline()
        string = regex0.sub('', string)  # removes the pos
        string = regex1.sub('', string)  # removes the ) and \n that's left
        string = float(string)/1000
        arr[(arr_size - 1) - y][x] = string  # because +/- is inverted in source


max_value = 0
for row in arr:
    if max(row) > max_value:
        max_value = max(row)

for row in arr:
    for value in row:
        value = round(value/max_value * 100)
        file1.write(str(value) + "  ")
    file1.write('\n')
    

file0.close()
file1.close()

print(max_value)
