from legacy.arr import Arr

class MockRead():
    def __init__(self):
        self.values = self.fill_values()

    def fill_values(self):
        return [10, 10, 10, 10, 10, 50, 45, 35, 35, 35, 40, 35, 30, 15, 20, 25, 20, 15, 10]

    def get_value(self):
        return int(self.values.pop())