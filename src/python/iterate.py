#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import numpy
import random
from colorama import Fore

MAX_VALUE = 9

class main():

    def createArray(self, xSize, ySize, xMax, yMax):
        arr = numpy.zeros((ySize, xSize)).tolist()
        arr[yMax][xMax] = MAX_VALUE

        for y in range(0, ySize):
            for x in range(0, xSize):
                if x == xMax and y == yMax:
                    continue
                arr[y][x] = MAX_VALUE - (abs(x - xMax) + abs(y - yMax))

        # for y in range(0, ySize):
        #     for x in range(0, xSize):
        #         if x == xMax and y == yMax:
        #             print(Fore.RED + "{:3d}".format(arr[y][x]), end=' ')
        #             continue
        #         print(Fore.RESET + "{:3d}".format(arr[y][x]), end=' ')
        #     print("")
        return arr

    def primitive(self, array):
        value = 0
        x = 0
        xValue = 0
        yValue = 0

        for row in array: 
            y = 0 #need to zero the y at the beginning of a new row
            for cell in row:
                if(cell > value):
                    value = cell
                    xValue = x
                    yValue = y
                y += 1
            x += 1
        print("HIGHETS VALUES WAS:" + str(value) + " on coordinate: x=" + str(xValue) + " y=" + str(yValue))

    def labyrinth(self,array):

        #values for the start position in the array
        a = random.randint(0, len(array[0])-2)
        b = random.randint(0, len(array)-2)

        #coordinates for 'value' in the array 
        x = 0
        y = 0

        #the highest value found
        value = float("-inf")

        #iterate through 3x3 array for startpoint
        for i in range(0,3 ):
            for j in range(0,3):
                if(array[a+i][b+j] > value):
                    value = array[a+i][b+j]
                    x = a+i
                    y = b+j

        #Check clockwise
        while(1):
            #EAST
            if(value < array[x+1][y]):
                x += 1
                value = array[x][y]

            #SOUTH EAST
            elif(value < array[x+1][y+1]):
                x += 1
                y += 1
                value = array[x][y]

            #SOUTH
            elif(value < array[x][y+1]):
                y += 1
                value = array[x][y]

            #SOUTH WEST
            elif(value < array[x-1][y+1]):
                x -= 1
                y -= 1            
                value = array[x][y]

            #WEST
            elif(value < array[x-1][y]):
                x -= 1
                value = array[x][y]

            #NORTH WEST
            elif(value < array[x-1][y-1]):          
                x -= 1
                y += 1
                value = array[x][y]
            #NORTH
            elif(value < array[x][y-1]):
                y -= 1
                value = array[x][y]
            #NORTH EAST
            elif(value < array[x+1][y-1]):
                x += 1
                y -= 1
                value = array[x][y]

            else:
                break

        print("HIGHETS VALUES WAS:" + str(value) + " on coordinate: x=" + str(x) + " y=" + str(y))

main = main()
array1 = main.createArray(1000, 1000, random.randint(0,999), random.randint(0,999))
array2 = main.createArray(1000, 1000, random.randint(0,999), random.randint(0,999))
array3 = main.createArray(1000, 1000, random.randint(0,999), random.randint(0,999))
start_time_p = time.time()
print("\nPRIMITIVE: ")
main.primitive(array1) 
main.primitive(array2)
main.primitive(array3)
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_p))
start_time_l = time.time()
print("\nLABYRINTH: ")
main.labyrinth(array1)
main.labyrinth(array2)
main.labyrinth(array3)
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_l))