from mars_rover.src.commands import Move, RotateLeft, RotateRight, NotACommand
from mars_rover.src.world import World


class MarsRoverController:

    def __init__(self, rover):
        self.commands = {'M': Move(rover),
                         'L': RotateLeft(rover),
                         'R': RotateRight(rover)}

    def input(self, cmd):
        for l in cmd:
            command = self.commands.get(l, NotACommand())
            self.execute(command)

    def execute(self, command):
        command.execute()


class MarsRover:

    def __init__(self, world=World()):
        self.compass = ['N', 'E', 'S', 'W']
        self.x, self.y = 0, 0
        self.world = world
        self.crashed = False

    def get_position(self):
        position = f"{self.x}:{self.y}:{self.get_direction()}"
        if self.crashed:
            position = 'O:' + position
        return position

    def get_direction(self):
        # The direction is the first point
        return self.compass[0]






















