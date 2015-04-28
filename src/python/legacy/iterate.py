#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import numpy
import random
from statistics import mean
from statistics import median
import sys
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

    def labyrinth_setup(self, array):
        # Create a set to be used for checking visited coordinates
        visited = set()

        # values for the start position in the array
        x = random.randint(0, len(array[0])-3)
        y = random.randint(0, len(array)-3)

        # the highest value found
        value = float("-inf")

        # Number of steps moved
        steps = 0

        return visited, x, y, len(array[0]) - 1, len(array) - 1, value, steps

    def labyrinth(self, array):
        visited, x, y, x_length, y_length, value, steps = self.labyrinth_setup(array)

        last_move = None
        finished = False

        # Check clockwise
        while not finished:
            # EAST
            if x < x_length and (last_move == None or last_move == 'E') and (x+1, y) not in visited:
                steps += 1
                visited.add((x+1, y))
                if value < array[x+1][y]:
                    x += 1
                    value = array[x][y]
                    last_move = 'E'

            # SOUTH EAST
            elif x < x_length and (last_move == None or last_move == 'SE') and y < y_length and (x+1, y+1) not in visited:
                steps += 1
                visited.add((x+1, y+1))
                if value < array[x+1][y+1]:
                    x += 1
                    y += 1
                    value = array[x][y]
                    last_move = 'SE'

            # SOUTH
            elif y < y_length and (last_move == None or last_move == 'S') and (x, y+1) not in visited:
                steps += 1
                visited.add((x, y+1))
                if value < array[x][y+1]:
                    y += 1
                    value = array[x][y]
                    last_move = 'S'

            # SOUTH WEST
            elif x > 0 and (last_move == None or last_move == 'SW') and y < y_length and (x-1, y+1) not in visited:
                steps += 1
                visited.add((x-1, y+1))
                if value < array[x-1][y+1]:
                    x -= 1
                    y -= 1
                    value = array[x][y]
                    last_move = 'SW'

            # WEST
            elif x > 0 and (last_move == None or last_move == 'W') and (x-1, y) not in visited:
                steps += 1
                visited.add((x-1, y))
                if value < array[x-1][y]:
                    x -= 1
                    value = array[x][y]
                    last_move = 'W'

            # NORTH WEST
            elif x > 0 and (last_move == None or last_move == 'NW') and y > 0 and (x-1, y-1) not in visited:
                steps += 1
                visited.add((x-1, y-1))
                if value < array[x-1][y-1]:
                    x -= 1
                    y += 1
                    value = array[x][y]
                    last_move = 'NW'

            # NORTH
            elif y > 0 and (last_move == None or last_move == 'N') and (x, y-1) not in visited:
                steps += 1
                visited.add((x, y-1))
                if value < array[x][y-1]:
                    y -= 1
                    value = array[x][y]
                    last_move = 'N'

            # NORTH EAST
            elif x < x_length and (last_move == None or last_move == 'NE') and y > 0 and (x+1, y-1) not in visited:
                steps += 1
                visited.add((x+1, y-1))
                if value < array[x+1][y-1]:
                    x += 1
                    y -= 1
                    value = array[x][y]
                    last_move = 'NE'

            elif last_move != None:
                last_move = None

            else:
                finished = True

        # self.print_results(value, x, y, steps)
        self.labyrinth_steps.append(steps)
        self.labyrinth_max_value.add(value)

    # Same as labyrinth(), but without diagonal movement
    def labyrinth2(self, array):
        visited, x, y, x_length, y_length, value, steps = self.labyrinth_setup(array)

        last_move = None
        finished = False

        # Check clockwise
        while not finished:
            # EAST
            if x < x_length and (last_move == None or last_move == 'EAST') and (x+1, y) not in visited:
                steps += 1
                visited.add((x+1, y))
                if value < array[x+1][y]:
                    x += 1
                    value = array[x][y]
                    last_move = 'EAST'

            # SOUTH
            elif y < y_length and (last_move == None or last_move == 'SOUTH') and (x, y+1) not in visited:
                steps += 1
                visited.add((x, y+1))
                if value < array[x][y+1]:
                    y += 1
                    value = array[x][y]
                    last_move = 'SOUTH'

            # WEST
            elif x > 0 and (last_move == None or last_move == 'WEST') and (x-1, y) not in visited:
                steps += 1
                visited.add((x-1, y))
                if value < array[x-1][y]:
                    x -= 1
                    value = array[x][y]
                    last_move = 'WEST'

            # NORTH
            elif y > 0 and (last_move == None or last_move == 'NORTH') and (x, y-1) not in visited:
                steps += 1
                visited.add((x, y-1))
                if value < array[x][y-1]:
                    y -= 1
                    value = array[x][y]
                    last_move = 'NORTH'

            elif last_move != None:
                last_move = None

            else:
                finished = True

        # self.print_results(value, x, y, steps)
        self.labyrinth2_steps.append(steps)
        self.labyrinth2_max_value.add(value)

    # Prints the provided value and its coordinates
    def print_results(self, value_found, x_pos, y_pos, steps=0):
        print("HIGHEST VALUE WAS:" + str(value_found) + " on coordinate: x: " +
              str(x_pos) + " y: " + str(y_pos) + " steps: " + str(steps))

    def test_labyrinth(self):
        print("LABYRINTH\t", end="")
        start_time = time.time()
        for i in range(0, self.num_arrays):
            self.labyrinth(self.arrays[i])
        print("Total time: %s seconds" % (time.time() - start_time))

    def test_labyrinth2(self):
        print("LABYRINTH 2\t", end="")
        start_time = time.time()
        for i in range(0, self.num_arrays):
            self.labyrinth2(self.arrays[i])
        print("Total time: %s seconds" % (time.time() - start_time))

    def test_all(self):
        print("\nArray size: " + str(self.array_size) + "\t\tArrays used: " +
              str(self.num_arrays) + "\n")

        self.test_labyrinth()
        self.test_labyrinth2()

        print("\n\t\tLabyrinth\tLabyrinth2")
        print("steps\tmax\t" + str(max(self.labyrinth_steps)) + "\t\t" +
              str(max(self.labyrinth2_steps)))
        print("\tmin\t" + str(min(self.labyrinth_steps)) + "\t\t" +
              str(min(self.labyrinth2_steps)))
        print("\tmean\t" + str(int(mean(self.labyrinth_steps))) + "\t\t" +
              str(int(mean(self.labyrinth2_steps))))
        print("\tmedian\t" + str(int(median(self.labyrinth_steps))) + "\t\t" +
              str(int(median(self.labyrinth2_steps))))
        print("\nvalue\tmax\t" + str(max(self.labyrinth_max_value)) + "\t\t" +
              str(max(self.labyrinth2_max_value)))
        print("\tmin\t" + str(min(self.labyrinth_max_value)) + "\t\t" +
              str(min(self.labyrinth2_max_value)))
        print()


# Main created with array size (square) and number of arrays
# Default is 500 for both, if nothing is given by sys arguments
arr_size = 500
arrays = 500

if len(sys.argv) > 1:
    if sys.argv[1].isdigit() and int(sys.argv[1]) > 0 and int(sys.argv[1]) < 1000:
        arr_size = int(sys.argv[1])
if len(sys.argv) > 2:
    if sys.argv[2].isdigit() and int(sys.argv[2]) > 0 and int(sys.argv[2]) < 1000:
        arrays = int(sys.argv[2])

main = main(arr_size, arrays)
main.create_arrays()

main.test_all()
