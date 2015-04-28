from arr import Arr


class Com():
    def __init__(self, x, y):
        self.arr = Arr()
        self.x_offset = x
        self.y_offset = y

    def get_value(self):
        return self.arr.get_value()

    def get_position(self):
        return self.arr.current_pos

    def set_position(self, x, y):
        self.arr.current_pos = (x, y)

    def move(self, coordinates, direction):
        x, y = coordinates
        
        if direction == 'EAST':
            x += self.x_offset
        elif direction == 'SOUTH':
            y -= self.y_offset
        elif direction == 'WEST':
            x -= self.x_offset
        elif direction == 'NORTH':
            y += self.y_offset

        self.set_position(x, y)
        return self.get_value()


