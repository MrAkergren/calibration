#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import random
from scom import SCom


class Main():
    def __init__(self):
        self.x_offset = 0.01
        self.y_offset = 0.01
        self.com = SCom(self.x_offset, self.y_offset)

    def labyrinth(self):
        # Create a set to be used for checking visited coordinates
        visited = set()

        # Initial coordinates
        x, y = self.com.get_coordinates()
        
        # Debug output
        print("Start pos: " + str(x) + ", " + str(y))

        # The highest value found
        start_value = value = self.com.get_value()

        steps = 0       # Checked for debugging
        last_move = None
        finished = False

        # Check clockwise
        # The array boundary checks are needed as long as an array is used as 
        # input to the Com class.
        while not finished:
            # EAST
            if (last_move == None or last_move == 'EAST') and (x+self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.com.move((x,y), 'EAST')
                visited.add((x+self.x_offset, y))
                if value < value_read :
                    x += self.x_offset
                    value = value_read
                    last_move = 'EAST'

            # SOUTH
            elif (last_move == None or last_move == 'SOUTH') and (x, y-self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.com.move((x,y), 'SOUTH')
                visited.add((x, y-self.y_offset))
                if value < value_read:
                    y -= self.y_offset
                    value = value_read
                    last_move = 'SOUTH'

            # WEST
            elif (last_move == None or last_move == 'WEST') and (x-self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.com.move((x,y), 'WEST')
                visited.add((x-self.x_offset, y))
                if value < value_read:
                    x -= self.x_offset
                    value = value_read
                    last_move = 'WEST'

            # NORTH
            elif (last_move == None or last_move == 'NORTH') and (x, y+self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.com.move((x,y), 'NORTH')
                visited.add((x, y+self.y_offset))
                if value < value_read:
                    y += self.y_offset
                    value = value_read
                    last_move = 'NORTH'

            elif last_move != None:
                last_move = None

            else:
                finished = True

        # Debug output
        print("End pos:\t" + str(x) + ", " + str(y))
        print("Steps:\t" + str(steps))
        print("Start value:\t" + str(start_value))
        print("End value:\t" + str(value))

main = Main()
main.labyrinth()
