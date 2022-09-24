from mars_rover.src.mars_rover import MarsRover,  MarsRoverController
from mars_rover.src.world import create_world


def test_rover_starts_on_a_world_with_no_obstacle_at_0_0():
    rover = MarsRover()
    assert rover.world.is_obstacle(0, 0) is False

def test_can_create_a_world_with_obstacle_at_1_0():
    world = create_world([(1, 0)])
    assert world.is_obstacle(1, 0) is True

def test_rover_can_be_created_on_world_with_obstacle_at_1_0():
    world = create_world([(1, 0)])
    rover = MarsRover(world=world)
    assert rover.world.is_obstacle(1, 0) is True

def test_rover_crashes_if_moving_onto_an_obstacle():
    world = create_world([(0, 1)])
    rover = MarsRover(world=world)
    controller = MarsRoverController(rover)
    cmd = 'M'
    controller.input(cmd)
    assert rover.get_position() == 'O:0:0:N'

def test_rover_moves_then_crashes_and_moves_no_further():
    world = create_world([(2, 0)])
    rover = MarsRover(world=world)
    controller = MarsRoverController(rover)
    cmd = 'RMMMLMMLMMLMMLMM'
    controller.input(cmd)
    assert rover.get_position() == 'O:1:0:E'