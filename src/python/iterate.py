#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import numpy
import random
from colorama import Fore

MAX_VALUE = 9

class main():
    def __init__(self, arraySize, numberOfArrays):
        self.arraySize = arraySize                  # Size of arrays to be generated
        self.numberOfArrays = numberOfArrays        # Number of arrays to be generated
        self.arrays = []                            # Holds the generated arrays
                
        self.labSteps = []                          # Holds number movements/steps for labyrinth()
        self.lab2Steps = []                         # Holds number movements/steps for labyrinth2()
        self.labMaxValue = set()                    # Holds max value(s) found in labyrinth()
        self.lab2MaxValue = set()                   # Holds max value(s) found in labyrinth2()

    def createArrays(self):
        for loop in range(0, self.numberOfArrays):
            self.arrays.append(main.createArray(self.arraySize, self.arraySize, random.randint(0,self.arraySize-1), random.randint(0,self.arraySize-1)))

    def createArray(self, xSize, ySize, xMax, yMax):
        arr = numpy.zeros((xSize, ySize)).tolist()
        arr[xMax][yMax] = MAX_VALUE

        for x in range(0, xSize):
            for y in range(0, ySize):
                if x == xMax and y == yMax:
                    continue
                arr[x][y] = MAX_VALUE - (abs(x - xMax) + abs(y - yMax))

        # self.printArray(arr, xSize, ySize, xMax, yMax)
        return arr

    def printArray(self, arr, xSize, ySize, xMax, yMax):
        for y in range(0, ySize):
            for x in range(0, xSize):
                if x == xMax and y == yMax:
                    print(Fore.RED + "{:3d}".format(arr[y][x]), end=' ')
                    continue
                print(Fore.RESET + "{:3d}".format(arr[y][x]), end=' ')
            print("")

    def labyrinth(self, array):
        # Creates an empty array with the same size as the one provided to the function,
        # used for keeping track of visited coordinates
        visited = numpy.zeros((len(array), len(array))).tolist()

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
        for i in range(0,3):
            for j in range(0,3):
                if(array[a+i][b+j] > value):
                    value = array[a+i][b+j]
                    x = a+i
                    y = b+j

        #Check clockwise
        while(True):
            #EAST
            if(x < xLength and not visited[x+1][y]):
                steps += 1
                if value < array[x+1][y]:
                    x += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y] = 1

            #SOUTH EAST
            elif(x < xLength and y < yLength and not visited[x+1][y+1]):
                steps += 1
                if value < array[x+1][y+1]:
                    x += 1
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y+1] = 1

            #SOUTH
            elif(y < yLength and not visited[x][y+1]):
                steps += 1
                if value < array[x][y+1]:
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y+1] = 1

            #SOUTH WEST
            elif(x > 0 and y < yLength and not visited[x-1][y+1]):
                steps += 1
                if value < array[x-1][y+1]:
                    x -= 1
                    y -= 1            
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y+1] = 1

            #WEST
            elif(x > 0 and not visited[x-1][y]):
                steps += 1
                if value < array[x-1][y]:
                    x -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y] = 1

            #NORTH WEST
            elif(x > 0 and y > 0 and not visited[x-1][y-1]):
                steps += 1
                if value < array[x-1][y-1]:
                    x -= 1
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y-1] = 1

            #NORTH
            elif(y > 0 and not visited[x][y-1]):
                steps += 1
                if value < array[x][y-1]:
                    y -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y-1] = 1

            #NORTH EAST
            elif(x < xLength and y > 0 and not visited[x+1][y-1]):
                steps += 1
                if value < array[x+1][y-1]:
                    x += 1
                    y -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y-1] = 1

            else:
                steps += 1
                break

        #self.printResults(value, x, y, steps)
        self.labSteps.append(steps)
        self.labMaxValue.add(value)

    # Same as labyrinth(), but without diagonal movement
    def labyrinth2(self, array):
        # Creates an empty array with the same size as the one provided to the function,
        # used for keeping track of visited coordinates
        visited = numpy.zeros((len(array), len(array))).tolist()

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
            if(x < xLength and not visited[x+1][y]):
                steps += 1
                if value < array[x+1][y]:
                    x += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y] = 1

            #SOUTH
            elif(y < yLength and not visited[x][y+1]):
                steps += 1
                if value < array[x][y+1]:
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y+1] = 1

            #WEST
            elif(x > 0 and not visited[x-1][y]):
                steps += 1
                if value < array[x-1][y]:
                    x -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y] = 1

            #NORTH
            elif(y > 0 and not visited[x][y-1]):
                steps += 1
                if value < array[x][y-1]:
                    y -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y-1] = 1

            else:
                steps += 1
                break

        #self.printResults(value, x, y, steps)
        self.lab2Steps.append(steps)
        self.lab2MaxValue.add(value)

    # Prints the provided value and its coordinates
    def printResults(self, valueFound, xPos, yPos, steps = 0):
        print("HIGHEST VALUE WAS:" + str(valueFound) + " on coordinate: x: " + str(xPos) + " y: " + str(yPos) + " steps: " + str(steps))

    def testPrimitive(self):
        print("\nPRIMITIVE: ")
        start_time = time.time()
        for i in range(0, min(3, self.numberOfArrays)):
            self.primitive(self.arrays[i])
        print("TOTAL TIME: %s seconds\n" % (time.time() - start_time))

    def testLabyrinth(self):
        print("\nLABYRINTH: ")
        start_time = time.time()
        for i in range(0, self.numberOfArrays):
            self.labyrinth(self.arrays[i])
        print("TOTAL TIME: %s seconds\n" % (time.time() - start_time))

    def testLabyrinth2(self):
        print("\nLABYRINTH 2: ")
        start_time = time.time()
        for i in range(0, self.numberOfArrays):
            self.labyrinth2(self.arrays[i])
        print("TOTAL TIME: %s seconds\n" % (time.time() - start_time))

    def testAll(self):
        self.testPrimitive()
        self.testLabyrinth()
        self.testLabyrinth2()

        print("\t\tLabyrinth\tLabyrinth2")
        print("max steps\t" + str(max(self.labSteps)) + "\t\t" + str(max(self.lab2Steps)))
        print("min steps\t" + str(min(self.labSteps)) + "\t\t" + str(min(self.lab2Steps)))
        print("avg steps\t" + str(int(sum(self.labSteps)/len(self.labSteps))) + "\t\t" + str(int(sum(self.lab2Steps)/len(self.lab2Steps))))
        print("max value\t" + str(max(self.labMaxValue)) + "\t\t" + str(max(self.lab2MaxValue)))
        print("min value\t" + str(min(self.labMaxValue)) + "\t\t" + str(min(self.lab2MaxValue)))


# Main created with array size (square) and number of arrays
main = main(500, 500)
main.createArrays()

main.testAll()
