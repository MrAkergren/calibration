#! /usr/bin/env python3
import numpy
import re
from datetime import date

arr = numpy.zeros((20, 20)).tolist()
regex0 = re.compile('\(\([-+]?[0-9]*\.?[0-9]+, [-+]?[0-9]*\.?[0-9]+\)\, ')
regex1 = re.compile('[^0-9 ]')
today = date.today()  #for naming
file0 = open('panel_array_test.txt', 'r')
file1 = open('gen_arr_%s.txt' %(today), 'w+')
for x in range(0, 20):
    for y in range(0, 20):
        string = file0.readline()
        string = regex0.sub('', string)  # removes the pos
        string = regex1.sub('', string)  # removes the ) and \n that's left
        string = float(string)/1000
        arr[19 - y][x] = string  # because +/- is inverted in source


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
