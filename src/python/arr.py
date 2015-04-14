import numpy
import random
from colorama import Fore


class Arr():
    def __init__(self):
        # super(Arr, self).__init__()
        # self.arg = arg
        self.MAX_VALUE = 9
        self.ySize = 1000
        self.xSize = 1000
        self.a = random.randint(0, self.xSize-1)
        self.b = random.randint(0, self.ySize-1)

        self.genArr = self.createArray(self.xSize, self.ySize, self.a, self.b)

    def createArray(self, xSize, ySize, xMax, yMax):
        arr = numpy.zeros((ySize, xSize)).tolist()
        arr[yMax][xMax] = self.MAX_VALUE

        for y in range(0, ySize):
            for x in range(0, xSize):
                if x == xMax and y == yMax:
                    continue
                arr[y][x] = self.MAX_VALUE - (abs(x - xMax) + abs(y - yMax))
        return arr

    def getValue(self, a, b):
        return self.genArr[a][b]

    def prettyPrint(self):
        for y in range(0, self.ySize):
            for x in range(0, self.xSize):
                if x == self.a and y == self.b:
                    print(Fore.RED + "{:3d}".format(self.genArr[y][x]), end=' ')
                    continue
                print(Fore.RESET + "{:3d}".format(self.genArr[y][x]), end=' ')
            print("")
