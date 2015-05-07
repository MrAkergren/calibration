from time import time
#from legacy.acom import Com

class Search:
    def __init__(self, serial_handler):
        self._SENSOR_BOUND = 1.0
        self._MAX_TIME = 300.0
        self.timeout = False
        self.com = serial_handler # Com(1,1)
        self.x_offset, self.y_offset = self.com.get_offset()

    def labyrinth(self):
        # Create a set to be used for checking visited coordinates
        visited = set()

        # Initial coordinates
        x, y = start_x, start_y = self.com.get_coordinates()

        # Get initial light value
        value = start_value = self.com.get_value()

        start_time = time()
        sun_sensor = True

        # Debug output
        print("Start pos: " + str(start_x) + ", " + str(start_y))

        steps = 0       # Checked for debugging
        last_move = None
        finished = False

        # Check clockwise
        # The array boundary checks are needed as long as an array is used as
        # input to the Com class.
        while not finished:
            # If coordinates has gone astray or search has been going on too long: abort
            if self._out_of_bounds(x, y) or self._search_timeout(start_time):
                break

            # for dir in ['EAST', 'SOUTH','WEST','NORTH']:
            #     _step(self, dir)

            # EAST
            elif (last_move is None or last_move == 'EAST') and (x+self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                try:
                    value_read = self._read_value((x, y), 'EAST')  #self.com.move((x, y), 'EAST')
                except:
                    sun_sensor = False
                    break
                visited.add((x+self.x_offset, y))
                if value < value_read:
                    x += self.x_offset
                    value = value_read
                    last_move = 'EAST'

            # SOUTH
            elif (last_move is None or last_move == 'SOUTH') and (x, y-self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                try:
                    value_read = self.com.move((x, y), 'SOUTH')
                except:
                    sun_sensor = False
                    break
                visited.add((x+self.x_offset, y))
                if value < value_read:
                    y -= self.x_offset
                    value = value_read
                    last_move = 'SOUTH'


            # WEST
            elif (last_move is None or last_move == 'WEST') and (x-self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                try:
                    value_read = self.com.move((x, y), 'WEST')
                except:
                    sun_sensor = False
                    break
                visited.add((x-self.x_offset, y))
                if value < value_read:
                    x -= self.x_offset
                    value = value_read
                    last_move = 'WEST'

            # NORTH
            elif (last_move is None or last_move == 'NORTH') and (x, y+self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                try:
                    value_read = self.com.move((x, y), 'NORTH')
                except:
                    sun_sensor = False
                    break
                visited.add((x, y+self.y_offset))
                if value < value_read:
                    y += self.y_offset
                    value = value_read
                    last_move = 'NORTH'

            elif last_move is not None:
                last_move = None

            else:
                finished = True

        # Search did not finish (x or y went out of bounds, or search timeout occured)
        if not finished or not sun_sensor:
            self.com.set_x_coordinate(str(start_x))
            self.com.set_y_coordinate(str(start_y))
            if self.timeout:
                print("Search timed out (> 5 minutes)")
            elif not sun_sensor:
                print("Sun sensor not active, reseting values.")
            else:
                print("Calibration went out of bounds")
            print("Sensor values are reset")


        # Debug output
        print("End pos:\t" + str(x) + ", " + str(y))
        print("Steps:\t" + str(steps))
        print("Start value:\t" + str(start_value))
        print("End value:\t" + str(value))

    def _out_of_bounds(self, x, y):
        return abs(x) > self._SENSOR_BOUND or abs(y) > self._SENSOR_BOUND

    def _search_timeout(self, start_time):
        return time()-start_time > self._MAX_TIME

