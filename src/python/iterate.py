#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import numpy
import random
from colorama import Fore

MAX_VALUE = 9


class main():
    def __init__(self, array_size, num_arrays):
        self.array_size = array_size    # Size of arrays to be generated
        self.num_arrays = num_arrays    # Number of arrays to generate
        self.arrays = []                # Holds the generated arrays

        self.labyrinth_steps = []   # Holds number of movements for labyrinth()
        self.labyrinth2_steps = []  # Holds number of movements for labyrinth2()
        self.labyrinth_max_value = set()   # Max value(s) found in labyrinth()
        self.labyrinth2_max_value = set()  # Max value(s) found in labyrinth2()

    def create_arrays(self):
        for loop in range(0, self.num_arrays):
            self.arrays.append(main.create_array(self.array_size,
                               self.array_size,
                               random.randint(0, self.array_size-1),
                               random.randint(0, self.array_size-1)))

    def create_array(self, x_size, y_size, x_max, y_max):
        arr = numpy.zeros((x_size, y_size)).tolist()
        arr[x_max][y_max] = MAX_VALUE

        for x in range(0, x_size):
            for y in range(0, y_size):
                if x == x_max and y == y_max:
                    continue
                arr[x][y] = MAX_VALUE - (abs(x - x_max) + abs(y - y_max))

        # self.print_array(arr, x_size, y_size, x_max, y_max)
        return arr

    def print_array(self, arr, x_size, y_size, x_max, y_max):
        for y in range(0, y_size):
            for x in range(0, x_size):
                if x == x_max and y == y_max:
                    print(Fore.RED + "{:3d}".format(arr[y][x]), end=' ')
                    continue
                print(Fore.RESET + "{:3d}".format(arr[y][x]), end=' ')
            print("")

    def labyrinth(self, array):
        # Creates an empty array with the same size as the parameter to
        # the function, used for keeping track of visited coordinates.
        visited = numpy.zeros((len(array), len(array))).tolist()

        # Length of array
        x_length = len(array[0]) - 1
        y_length = len(array) - 1

        # values for the start position in the array
        a = random.randint(0, len(array[0])-3)
        b = random.randint(0, len(array)-3)

        # coordinates for 'value' in the array
        x = 0
        y = 0

        # the highest value found
        value = float("-inf")

        # Number of steps moved
        steps = 0

        # iterate through 3x3 array for startpoint
        for i in range(0, 3):
            for j in range(0, 3):
                if(array[a+i][b+j] > value):
                    value = array[a+i][b+j]
                    x = a+i
                    y = b+j

        # Check clockwise
        while(True):
            # EAST
            if(x < x_length and not visited[x+1][y]):
                steps += 1
                if value < array[x+1][y]:
                    x += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y] = 1

            # SOUTH EAST
            elif(x < x_length and y < y_length and not visited[x+1][y+1]):
                steps += 1
                if value < array[x+1][y+1]:
                    x += 1
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y+1] = 1

            # SOUTH
            elif(y < y_length and not visited[x][y+1]):
                steps += 1
                if value < array[x][y+1]:
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y+1] = 1

            # SOUTH WEST
            elif(x > 0 and y < y_length and not visited[x-1][y+1]):
                steps += 1
                if value < array[x-1][y+1]:
                    x -= 1
                    y -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y+1] = 1

            # WEST
            elif(x > 0 and not visited[x-1][y]):
                steps += 1
                if value < array[x-1][y]:
                    x -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y] = 1

            # NORTH WEST
            elif(x > 0 and y > 0 and not visited[x-1][y-1]):
                steps += 1
                if value < array[x-1][y-1]:
                    x -= 1
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y-1] = 1

            # NORTH
            elif(y > 0 and not visited[x][y-1]):
                steps += 1
                if value < array[x][y-1]:
                    y -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y-1] = 1

            # NORTH EAST
            elif(x < x_length and y > 0 and not visited[x+1][y-1]):
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

        # self.print_results(value, x, y, steps)
        self.labyrinth_steps.append(steps)
        self.labyrinth_max_value.add(value)

    # Same as labyrinth(), but without diagonal movement
    def labyrinth2(self, array):
        # Creates an empty array with the same size as the parameter to
        # the function, used for keeping track of visited coordinates.
        visited = numpy.zeros((len(array), len(array))).tolist()

        # Length of array
        x_length = len(array[0]) - 1
        y_length = len(array) - 1

        # values for the start position in the array
        a = random.randint(0, len(array[0])-3)
        b = random.randint(0, len(array)-3)

        # coordinates for 'value' in the array
        x = 0
        y = 0

        # the highest value found
        value = float("-inf")

        # Number of steps moved
        steps = 0

        # iterate through 3x3 array for startpoint
        for i in range(0, 3):
            for j in range(0, 3):
                if(array[a+i][b+j] > value):
                    value = array[a+i][b+j]
                    x = a+i
                    y = b+j

        # Check clockwise
        while(True):
            # EAST
            if(x < x_length and not visited[x+1][y]):
                steps += 1
                if value < array[x+1][y]:
                    x += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x+1][y] = 1

            # SOUTH
            elif(y < y_length and not visited[x][y+1]):
                steps += 1
                if value < array[x][y+1]:
                    y += 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x][y+1] = 1

            # WEST
            elif(x > 0 and not visited[x-1][y]):
                steps += 1
                if value < array[x-1][y]:
                    x -= 1
                    value = array[x][y]
                    visited[x][y] = 1
                else:
                    visited[x-1][y] = 1

            # NORTH
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

        # self.print_results(value, x, y, steps)
        self.labyrinth2_steps.append(steps)
        self.labyrinth2_max_value.add(value)

    # Prints the provided value and its coordinates
    def print_results(self, value_found, x_pos, y_pos, steps=0):
        print("HIGHEST VALUE WAS:" + str(value_found) + " on coordinate: x: " +
              str(x_pos) + " y: " + str(y_pos) + " steps: " + str(steps))

    def test_labyrinth(self):
        print("\nLABYRINTH: ")
        start_time = time.time()
        for i in range(0, self.num_arrays):
            self.labyrinth(self.arrays[i])
        print("TOTAL TIME: %s seconds\n" % (time.time() - start_time))

    def test_labyrinth2(self):
        print("\nLABYRINTH 2: ")
        start_time = time.time()
        for i in range(0, self.num_arrays):
            self.labyrinth2(self.arrays[i])
        print("TOTAL TIME: %s seconds\n" % (time.time() - start_time))

    def test_all(self):
        self.test_labyrinth()
        self.test_labyrinth2()

        print("\t\tLabyrinth\tLabyrinth2")
        print("max steps\t" + str(max(self.labyrinth_steps)) + "\t\t" +
              str(max(self.labyrinth2_steps)))
        print("min steps\t" + str(min(self.labyrinth_steps)) + "\t\t" +
              str(min(self.labyrinth2_steps)))
        print("avg steps\t" +
              str(int(sum(self.labyrinth_steps)/len(self.labyrinth_steps))) +
              "\t\t" +
              str(int(sum(self.labyrinth2_steps)/len(self.labyrinth2_steps))))
        print("max value\t" + str(max(self.labyrinth_max_value)) + "\t\t" +
              str(max(self.labyrinth2_max_value)))
        print("min value\t" + str(min(self.labyrinth_max_value)) + "\t\t" +
              str(min(self.labyrinth2_max_value)))


# Main created with array size (square) and number of arrays
main = main(500, 500)
main.create_arrays()

main.test_all()
