from mars_rover.src.commands import Move, RotateLeft, RotateRight


class MarsRoverController:

    def __init__(self, rover):
        self.commands = {'M': Move(rover),
                         'L': RotateLeft(rover),
                         'R': RotateRight(rover)}

    def input(self, cmd):
        for l in cmd:
            command = self.commands[l]
            self.execute(command)

    def execute(self, command):
        command.execute()


class MarsRover:

    def __init__(self):

        self.compass = ['N', 'E', 'S', 'W']
        self.x = 0
        self.y = 0

    def get_position(self):
        return f"{self.x}:{self.y}:{self.get_direction()}"

    def get_direction(self):
        # The direction is the first point
        return self.compass[0]






















