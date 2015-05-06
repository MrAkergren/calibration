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
            #     _alg(self, dir)

            # EAST
            elif (last_move is None or last_move == 'EAST') and (x+self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                value_read = self._read_value((x, y), 'EAST')  #self.com.move((x, y), 'EAST')
                if value_read:
                    visited.add((x+self.x_offset, y))
                    if value < value_read:
                        x += self.x_offset
                        value = value_read
                        last_move = 'EAST'
                else:
                    sun_sensor = False
                    break

            # SOUTH
            elif (last_move is None or last_move == 'SOUTH') and (x, y-self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                value_read = self._read_value((x, y), 'SOUTH') #self.com.move((x, y), 'SOUTH')
                if value_read:
                    visited.add((x+self.x_offset, y))
                    if value < value_read:
                        x += self.x_offset
                        value = value_read
                        last_move = 'SOUTH'
                else:
                    sun_sensor = False
                    break

            # WEST
            elif (last_move is None or last_move == 'WEST') and (x-self.x_offset, y) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.com.move((x, y), 'WEST')
                visited.add((x-self.x_offset, y))
                if value < value_read:
                    x -= self.x_offset
                    value = value_read
                    last_move = 'WEST'

            # NORTH
            elif (last_move is None or last_move == 'NORTH') and (x, y+self.y_offset) not in visited:
                steps += 1      # Counted for debugging
                value_read = self.com.move((x, y), 'NORTH')
                visited.add((x, y+self.y_offset))
                if value < value_read:
                    y += self.y_offset
                    value = value_read
                    last_move = 'NORTH'

            elif not sun_sensor:
                print("Sun sensor not active")
                break

            elif last_move is not None:
                last_move = None

            else:
                finished = True

        # Search did not finish (x or y went out of bounds, or search timeout occured)
        if not finished and sun_sensor:
            self.com.set_x_coordinate(start_x)
            self.com.set_y_coordinate(start_y)
            if self.timeout:
                print("Search timed out (> 5 minutes)")
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

    def _read_value(self, coor, dir):
        try:
            return self.com.move(coor, dir)
        except:
            return False

    # def _alg(self, dir):
    #        if (last_move is None or last_move == dir) and (x+self.x_offset, y) not in visited:
    #             value_read = self._read_value((x, y), dir)
    #             if value_read:
    #                 visited.add((x+self.x_offset, y))
    #                 if value < value_read:
    #                     x += self.x_offset
    #                     value = value_read
    #                     last_move = dir
    #             else:
    #                 sun_sensor = False

