#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from time import sleep, strftime
from serial_handler import SerialHandler
import sys

d = strftime("%Y-%m-%d_%H.%M")


args = sys.argv

square_size = args[1]
start_x = args[2]
start_y = args[3]
panelname = args[4]

offset = 0.01

print("An automatic script on panel \'" + panelname + "\' is now starting.\n" 
    "The size of the generated arry will be: " + square_size +"x" + square_size + " \n" + 
    "The starting position will be: " + start_x +","+ start_y + "\n")


# values = {}
values = []

# sh = SerialHandler(0.01, 0.01)
# sh.connect_devices()

# original_coords = sh.get_coordinates()
# sh.set_coordinates(str(start_x), str(start_y))
# sleep(2)

# current_pos = sh.get_coordinates()
# print("Current coordinates:\n %.4f, %.4f" % current_pos)

# x_pos, y_pos = current_pos
# # for x in range(0, square_size):
# #     x_pos = start_x + offset * x
# #     sh.set_x_coordinate(str(x_pos)) 

# #     for y in range(0, square_size):
# #         y_pos = start_y + offset * y
# #         sh.set_y_coordinate(str(y_pos))

# #         values[(round(x_pos, 3), round(y_pos, 3))] = sh.get_value()

# for x in range(0, square_size):
#     print("\t--- New x set: %d ---" % x)
#     x_pos = start_x + offset * x
#     sh.set_x_coordinate(str(x_pos))
#     x_arr = []
#     values.append(x_arr)
#     for y in range(0, square_size):
#         y_pos = start_y + offset * y
#         sh.set_y_coordinate(str(y_pos))
#         current_value = sh.get_value
#         print("Value read: " + str(current_value))
#         x_arr.append( ((round(x_pos, 3), round(y_pos, 3)), current_value) )

# print(values)

# fh = open("test_results.txt", "w+")
# # for pos, value in values:
# #     fh.write("" + str(pos) + "\t" + value + "\n")

# for row in values:
#     for value in row:
#         fh.write(str(value) + "\n")

# sh.set_coordinates(str(original_coords[0]), str(original_coords[1]))
# fh.close()


fh = open("test_results.txt", "w+")
fh.close()