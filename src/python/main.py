#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import random
from com import Com


class Main():
    def __init__(self):
        super(Main, self).__init__()
        self.panel = Com()

    def labyrinth(self):

        # values for the start position in the array
        a = random.randint(0, 997)
        b = random.randint(0, 997)

        # coordinates for 'value' in the array
        x = 0
        y = 0

        # the highest value found
        value = float("-inf")

        # iterate through 3x3 array for startpoint
        for i in range(0, 3):
            for j in range(0, 3):
                if(self.panel.get_value(i, j) > value):
                    value = self.panel.get_value(i, j)
                    self.panel.set_x_coordinate(i)
                    self.panel.set_y_coordinate(j)

        return value

        # Check clockwise
#          while(1):
#              # EAST
#              if(value < array[x+1][y]):
#                  x += 1
#                  value = array[x][y]

#              # SOUTH EAST
#              elif(value < array[x+1][y+1]):
#                  x += 1
#                  y += 1
#                  value = array[x][y]

#              # SOUTH
#              elif(value < array[x][y+1]):
#                  y += 1
#                  value = array[x][y]

#              # SOUTH WEST
#              elif(value < array[x-1][y+1]):
#                  x -= 1
#                  y -= 1
#                  value = array[x][y]

#              # WEST
#              elif(value < array[x-1][y]):
#                  x -= 1
#                  value = array[x][y]

#              # NORTH WEST
#              elif(value < array[x-1][y-1]):
#                  x -= 1
#                  y += 1
#                  value = array[x][y]
#              # NORTH
#              elif(value < array[x][y-1]):
#                  y -= 1
#                  value = array[x][y]
#              # NORTH EAST
#              elif(value < array[x+1][y-1]):
#                  x += 1
#                  y -= 1
#                  value = array[x][y]

#              else:
#                  break

#          print("HIGHETS VALUES WAS:" + str(value) + " on coordinate: x=" + str(x) + " y=" + str(y))

main = Main()
a = main.labyrinth()
print(a)
