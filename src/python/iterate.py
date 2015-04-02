#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import numpy
import random
from colorama import Fore

MAX_VALUE = 9

class main():
    def __init__(self):
        self.labSteps = []
        self.lab2Steps = []
        self.labMaxValue = set()
        self.lab2MaxValue = set()


    def createArray(self, xSize, ySize, xMax, yMax):
        arr = numpy.zeros((xSize, ySize)).tolist()
        arr[xMax][yMax] = MAX_VALUE

        for x in range(0, xSize):
            for y in range(0, ySize):
                if x == xMax and y == yMax:
                    continue
                arr[x][y] = MAX_VALUE - (abs(x - xMax) + abs(y - yMax))

        # for y in range(0, ySize):
        #     for x in range(0, xSize):
        #         if x == xMax and y == yMax:
        #             print(Fore.RED + "{:3d}".format(arr[y][x]), end=' ')
        #             continue
        #         print(Fore.RESET + "{:3d}".format(arr[y][x]), end=' ')
        #     print("")
        return arr

    def primitive(self, array):
        value = float("-inf")
        x = 0
        xValue = 0
        yValue = 0
        steps = 0

        for row in array: 
            y = 0 #need to zero the y at the beginning of a new row
            for cell in row:
                if(cell > value):
                    value = cell
                    xValue = x
                    yValue = y
                steps += 1
                y += 1
            x += 1

        self.printResults(value, xValue, yValue, steps)

    def labyrinth(self,array):
        # Length of array
        xLength = len(array[0]) - 1
        yLength = len(array) - 1

        #values for the start position in the array
        a = random.randint(0, len(array[0])-3)
        b = random.randint(0, len(array)-3)

        #coordinates for 'value' in the array 
        x = 0
        y = 0

        #the highest value found
        value = float("-inf")

        # Number of steps moved
        steps = 0

        #iterate through 3x3 array for startpoint
        for i in range(0,3 ):
            for j in range(0,3):
                if(array[a+i][b+j] > value):
                    value = array[a+i][b+j]
                    x = a+i
                    y = b+j

        #Check clockwise
        while(True):
            #EAST
            if(x < xLength and value < array[x+1][y]):
                x += 1
                value = array[x][y]
                steps += 1

            #SOUTH EAST
            elif(x < xLength and y < yLength and value < array[x+1][y+1]):
                x += 1
                y += 1
                value = array[x][y]
                steps += 2

            #SOUTH
            elif(y < yLength and value < array[x][y+1]):
                y += 1
                value = array[x][y]
                steps += 3

            #SOUTH WEST
            elif(x > 0 and y < yLength and value < array[x-1][y+1]):
                x -= 1
                y -= 1            
                value = array[x][y]
                steps += 4

            #WEST
            elif(x > 0 and value < array[x-1][y]):
                x -= 1
                value = array[x][y]
                steps += 5

            #NORTH WEST
            elif(x > 0 and y > 0 and value < array[x-1][y-1]):          
                x -= 1
                y += 1
                value = array[x][y]
                steps += 6

            #NORTH
            elif(y > 0 and value < array[x][y-1]):
                y -= 1
                value = array[x][y]
                steps += 7

            #NORTH EAST
            elif(x < xLength and y > 0 and value < array[x+1][y-1]):
                x += 1
                y -= 1
                value = array[x][y]
                steps += 8

            else:
                steps += 1
                break

        #self.printResults(value, x, y, steps)
        self.labSteps.append(steps)
        self.labMaxValue.add(value)

    def labyrinth2(self,array):
        # Length of array
        xLength = len(array[0]) - 1
        yLength = len(array) - 1

        #values for the start position in the array
        a = random.randint(0, len(array[0])-3)
        b = random.randint(0, len(array)-3)

        #coordinates for 'value' in the array 
        x = 0
        y = 0

        #the highest value found
        value = float("-inf")

        # Number of steps moved
        steps = 0

        #iterate through 3x3 array for startpoint
        for i in range(0,3 ):
            for j in range(0,3):
                if(array[a+i][b+j] > value):
                    value = array[a+i][b+j]
                    x = a+i
                    y = b+j

        #Check clockwise
        while(True):
            #EAST
            if(x < xLength and value <= array[x+1][y]):
                x += 1
                value = array[x][y]
                steps += 1

            #SOUTH
            elif(y < yLength and value <= array[x][y+1]):
                y += 1
                value = array[x][y]
                steps += 2

            #WEST
            elif(x > 0 and value <= array[x-1][y]):
                x -= 1
                value = array[x][y]
                steps += 3

            #NORTH
            elif(y > 0 and value <= array[x][y-1]):
                y -= 1
                value = array[x][y]
                steps += 4

            else:
                steps += 1
                break

        #self.printResults(value, x, y, steps)
        self.lab2Steps.append(steps)
        self.lab2MaxValue.add(value)

    # Prints the provided value and its coordinates
    def printResults(self, valueFound, xPos, yPos, steps = 0):
        print("HIGHEST VALUE WAS:" + str(valueFound) + " on coordinate: x: " + str(xPos) + " y: " + str(yPos) + " steps: " + str(steps))


main = main()
arrays = []
RANGE_SIZE = 500
ARRAY_SIZE = 500

for loop in range(0, RANGE_SIZE):
    arrays.append(main.createArray(ARRAY_SIZE, ARRAY_SIZE, random.randint(0,ARRAY_SIZE-1), random.randint(0,ARRAY_SIZE-1)))

print("\nPRIMITIVE: ")
start_time_p = time.time()
for loop in range(0, 3):
    main.primitive(arrays[loop])
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_p))

print("\nLABYRINTH: ")
start_time_l = time.time()
for loop in range(0, RANGE_SIZE):
    main.labyrinth(arrays[loop])
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_l))

print("\nLABYRINTH 2: ")
start_time_l2 = time.time()
for loop in range(0, RANGE_SIZE):
    main.labyrinth2(arrays[loop])
print("TOTAL TIME: %s seconds\n" % (time.time() - start_time_l2))

print("\t\tLabyrinth\tLabyrinth2")
print("max steps\t" + str(max(main.labSteps)) + "\t\t" + str(max(main.lab2Steps)))
print("min steps\t" + str(min(main.labSteps)) + "\t\t" + str(min(main.lab2Steps)))
print("avg steps\t" + str(int(sum(main.labSteps)/len(main.labSteps))) + "\t\t" + str(int(sum(main.lab2Steps)/len(main.lab2Steps))))
