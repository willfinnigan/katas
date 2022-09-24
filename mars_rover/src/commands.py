from abc import ABC, abstractmethod
from mars_rover.src.movements import move_north, move_east, move_south, move_west

class Command(ABC):

    @abstractmethod
    def __init__(self, rover):
        self.rover = rover

    @abstractmethod
    def execute(self):
        pass


class RotateLeft(Command):

    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        end_direction = self.rover.compass.pop(3)
        self.rover.compass = [end_direction] + self.rover.compass


class RotateRight(Command):

    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        end_direction = self.rover.compass.pop(0)
        self.rover.compass = self.rover.compass + [end_direction]


class Move(Command):
    def __init__(self, rover):
        self.rover = rover
        self.movements = {'N': move_north,
                          'E': move_east,
                          'S': move_south,
                          'W': move_west}

    def execute(self):
        move = self._get_movement()
        self.rover.x, self.rover.y = move(self.rover.x, self.rover.y)

    def _get_movement(self):
        d = self.rover.get_direction()
        move = self.movements[d]
        return move