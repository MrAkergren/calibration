#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy
from colorama import Fore

MAX_VALUE = 9

def getValues():
	xSize = ySize = xMax = yMax = -1
	while not xSize > 0:
		xSize = int(input("Size x: "))
	while not ySize > 0:
		ySize = int(input("Size y: "))
	while not (xMax > -1 and xMax < xSize):
		xMax = int(input("Max x: "))
	while not (yMax > -1 and yMax < ySize):
		yMax = int(input("Max y: "))

	createArray(xSize, ySize, xMax, yMax)

def createArray(xSize, ySize, xMax, yMax):
	arr = numpy.zeros((ySize, xSize)).tolist()
	arr[yMax][xMax] = MAX_VALUE

	for y in range(0, ySize):
		for x in range(0, xSize):
			if x == xMax and y == yMax:
				continue
			arr[y][x] = MAX_VALUE - (abs(x - xMax) + abs(y - yMax))

	#for y in range(0, ySize):
	#	print(arr[y])

	for y in range(0, ySize):
		for x in range(0, xSize):
			if x == xMax and y == yMax:
				print(Fore.RED + "{:3d}".format(arr[y][x]), end=' ')
				continue
			print(Fore.RESET + "{:3d}".format(arr[y][x]), end=' ')
		print("")


getValues()