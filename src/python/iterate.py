#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import numpy
from colorama import Fore
import random

MAX_VALUE = 9
    
# array = ([  [0, 0, 0, 0, 0],
#             [0, 1, 1, 1, 0],
#             [0, 1, 5, 1, 0],
#             [0, 1, 4, 10, 0],
#             [0, 1, 4, 1, 0]     ])

# cols = len(array[0])
# rows = len(array)

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
            x += 1
            y = 0 #need to zero the y at the beginning of a new row
            for cell in row:
                y += 1
                if(cell > value):
                    value = cell
                    xValue = x
                    yValue = y


        print("\nPRIMITIVE: ")
        print("HIGHETS VALUES WAS:" + str(value) + " on coordinate: x=" + str(xValue) + " y=" + str(yValue))
       

    def labyrinth(self,array):
        
        # cols = 
        # rows = len(array)

        #values for the start position in the array
        a = random.randint(0, len(array[0])-2)
        b = random.randint(0, len(array)-2)

        #coordinates for the highest current value in the array 
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

        #print("DEVELOP INFORMATION ---- X=" + str(x)+" Y="+str(y)+"\n VALUE="+ str(value))

        while(1):
            #EAST
            if(value < array[x+1][y]):
                value = array[x+1][y]
                x += 1

            #SOUTH EAST
            elif(value < array[x+1][y+1]):
                value = array[x+1][y+1]
                x += 1
                y += 1

            #SOUTH
            elif(value < array[x][y+1]):
                value = array[x][y+1]
                y += 1
            
            #SOUTH WEST
            elif(value < array[x-1][y+1]):
                x -= 1
                y -= 1            

            #WEST
            elif(value < array[x-1][y]):
                value = array[x-1][y]
                x -= 1

            #NORTH WEST
            elif(value < array[x-1][y-1]):
                value = array[x-1][y+1]
                x -= 1
                y += 1

            #NORTH
            elif(value < array[x][y-1]):
                value = array[x][y-1]
                y -= 1

            #NORTH EAST
            elif(value < array[x+1][y-1]):
                value =array[x+1][y-1]
                x += 1
                y -= 1

            else:
                break



        print("\nLABYRINTH: ")
        print("HIGHETS VALUES WAS:" + str(value) + " on coordinate: x=" + str(x) + " y=" + str(y))
        
    def stepRight(self, y):
        y += 1

        return(y)   

    def stepDown(self, x):
        x += 1

        return(x)

main = main()
array1 = main.createArray(1000, 1000, random.randint(0,999), random.randint(0,999))
array2 = main.createArray(1000, 1000, random.randint(0,999), random.randint(0,999))
array3 = main.createArray(1000, 1000, random.randint(0,999), random.randint(0,999))
start_time_p = time.time()
main.primitive(array1) 
main.primitive(array2)
main.primitive(array3)
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_p))
start_time_l = time.time()
main.labyrinth(array1)
main.labyrinth(array2)
main.labyrinth(array3)
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_l))