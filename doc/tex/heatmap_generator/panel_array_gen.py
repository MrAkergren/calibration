#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from time import sleep
from serial_handler import SerialHandler
import sys


args = sys.argv

square_size = int(args[1])
start_x = float(args[2])
start_y = float(args[3])
panelname = args[4]

offset = 0.01

print("An automatic script on panel \'" + panelname + "\' is now starting.\n" 
    "The size of the generated arry will be: " + str(square_size) +"x" + str(square_size) + " \n" + 
    "The starting position will be: " + str(start_x) +","+ str(start_y) + "\n")


values = []

sh = SerialHandler()
sh.connect_devices()

original_coords = sh.get_coordinates()
print("The panel's original coordinates were:\nx:\t%f\ny:\t%f" % original_coords)
sh.set_coordinates(str(start_x), str(start_y))
sleep(2)

current_pos = sh.get_coordinates()
print("Current coordinates:\n %.4f, %.4f" % current_pos)

for x in range(0, square_size):
    print("\t--- New x set: " + str(x) + " (of " + str(square_size-1) + ") ---")
    x_pos = start_x + offset * x
    sh.set_x_coordinate(str(x_pos))
    x_arr = []
    values.append(x_arr)
    for y in range(0, square_size):
        y_pos = start_y + offset * y
        sh.set_y_coordinate(str(y_pos))
        sh.wait_for_panel_position()
        current_value = sh.get_value()
        print("Value read: " + str(current_value))
        x_arr.append( ((round(x_pos, 3), round(y_pos, 3)), current_value) )

print(values)

fh = open("test_results.txt", "w+")

for row in values:
    for value in row:
        fh.write(str(value) + "\n")

sh.set_coordinates(str(original_coords[0]), str(original_coords[1]))
fh.close()
