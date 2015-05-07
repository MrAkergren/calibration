import numpy
import random
from colorama import Fore


class Arr():
    def __init__(self):
        # super(Arr, self).__init__()
        # self.arg = arg
        self.MAX_VALUE = 100
        self.x_size = 7
        self.y_size = 7
        self.a = random.randint(0, self.x_size-2)
        self.b = random.randint(0, self.y_size-2)

        self.gen_arr = self.create_array1()#(self.x_size, self.y_size, self.a, self.b)
        self.pretty_print()
        self.current_pos = (1, 1) #(random.randint(0, self.x_size-1), random.randint(0, self.y_size-1))

    def create_array(self, x_size, y_size, x_max, y_max):
        arr = numpy.zeros((x_size, y_size)).tolist()
        arr[x_max][y_max] = self.MAX_VALUE

        for x in range(0, x_size):
            for y in range(0, y_size):
                if x == x_max and y == y_max:
                    continue
                arr[x][y] = self.MAX_VALUE - (abs(x - x_max) + abs(y - y_max))

        return arr


    def get_value(self):
        x, y = self.current_pos
        if x < 0 or x >= self.x_size or y < 0 or y >= self.y_size:
            return float("-inf")
        else:
            return self.gen_arr[x][y]

    def pretty_print(self):
        for x in range(0, self.x_size):
            for y in range(0, self.y_size):
                if x == self.a and y == self.b:
                    print(Fore.RED + "{:3d}".format(self.gen_arr[x][y]), end=' ')
                    continue
                print(Fore.RESET + "{:3d}".format(self.gen_arr[x][y]), end=' ')
            print("")

    def set_x(self, num):
        x, y = self.current_pos
        x = num
        self.current_pos = (x, y)

    def set_y(self, num):
        x, y = self.current_pos
        y = num
        self.current_pos = (x, y)

    def create_array1(self):
        a = [[ 84,  84,  84,  84,  84,  84,  84,  84,  84,  84],
             [84,  85,  85,  85,  90 , 91,  92 , 93 , 94 , 93],
             [84 , 85,  85,  95,  91 , 92, 93  ,94  ,95  ,94],
             [84 , 85,  85,  91,  92 , 93, 94  ,95 , 96  ,95],
             [84 , 85,  85,  92,  93 , 94,  95 , 96,  97 , 96],
             [94 , 91,  92,  93,  94,  95,  96 , 97,  98,  97],
             [91  ,92,  93,  94,  95,  96,  97,  98,  99 , 98],
             [92 , 93,  94,  95,  96,  97,  98,  99 ,100,  99],
             [91 , 92,  93,  94,  95,  96,  97,  98 , 99,  98],
             [90 , 91,  92,  93,  94,  95,  96,  97  ,98,  97],
            ]

        b = [[83,  83,  83,  83,  83, 84, 84],
            [83, 84, 85, 85, 85, 85, 84],
            [83, 85, 85, 85, 85, 85, 84],
            [83, 85, 85, 85, 85, 85, 84],
            [83, 85, 85, 85, 85, 85, 84],
            [84, 85, 85, 85, 85, 100, 84],
            [84,  84,  84,  84,  84, 84, 84]]

        return b