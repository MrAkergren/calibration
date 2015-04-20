#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import random
from com import Com


class Main():
    def __init__(self):
        self.x_offset = 1
        self.y_offset = 1
        self.panel = Com(self.x_offset, self.y_offset)

    def labyrinth(self):
        # Create a set to be used for checking visited coordinates
        visited = set()

        # Initial coordinates
        x, y = self.panel.get_position()
        
        # Debug output
        print("Start pos: " + str(x) + ", " + str(y))

        # The highest value found
        value = self.panel.get_value()
        start_value = value

        steps = 0
        last_move = None
        x_length = y_length = len(self.panel.arr.gen_arr)-1

        # Check clockwise
        # The array boundary checks are needed as long as an array is used as 
        # input to the Com class.
        while(True):
            # EAST
            if x < len(self.panel.arr.gen_arr)-1 and (last_move == None or last_move == 'EAST') and (x+self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.panel.move((x,y), 'EAST')
                visited.add((x+self.x_offset, y))
                if value < value_read :
                    x += self.x_offset
                    value = value_read
                    last_move = 'EAST'

            # SOUTH
            elif y > 0 and (last_move == None or last_move == 'SOUTH') and (x, y-self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.panel.move((x,y), 'SOUTH')
                visited.add((x, y-self.y_offset))
                if value < value_read:
                    y -= self.y_offset
                    value = value_read
                    last_move = 'SOUTH'

            # WEST
            elif x > 0 and (last_move == None or last_move == 'WEST') and (x-self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.panel.move((x,y), 'WEST')
                visited.add((x-self.x_offset, y))
                if value < value_read:
                    x -= self.x_offset
                    value = value_read
                    last_move = 'WEST'

            # NORTH
            elif y < len(self.panel.arr.gen_arr)-1 and (last_move == None or last_move == 'NORTH') and (x, y+self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.panel.move((x,y), 'NORTH')
                visited.add((x, y+self.y_offset))
                if value < value_read:
                    y += self.y_offset
                    value = value_read
                    last_move = 'NORTH'

            elif last_move != None:
                last_move = None

            else:
                break

        # Debug output
        print("End pos:\t" + str(x) + ", " + str(y))
        print("Steps:\t" + str(steps))
        print("Start value:\t" + str(start_value))
        print("End value:\t" + str(value))

main = Main()
main.labyrinth()
