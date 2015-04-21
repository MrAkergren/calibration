from arr import Arr


class Com(object):
    def __init__(self):
        super(Com, self).__init__()
        self.arr = Arr()
        self.x = 0
        self.y = 0

    def get_value(self):
        return self.arr.getValue(self.x, self.y)

    def get_this_value(self, x, y):
        return self.arr.getValue(x, y)

    def get_x_coordinate(self):
        return self.x

    def get_y_coordinate(self):
        return self.y

    def set_x_coordinate(self, num):
        self.x = num

    def set_y_coordinate(self, num):
        self.y = num

    def step_east(self):
        self.x += 1

    def step_south_east(self):
        self.x += 1
        self.y += 1

    def step_south(self):
        self.y += 1

    def step_south_west(self):
        self.x -= 1
        self.y += 1

    def step_west(self):
        self.x -= 1

    def step_north_west(self):
        self.x -= 1
        self.y += 1

    def step_north(self):
        self.y -= 1

    def step_north_east(self):
        self.x += 1
        self.y -= 1
