from dataclasses import dataclass, field
from typing import List


@dataclass
class Obstacle:
    x: int
    y: int

@dataclass
class World:
    list_obstacles: List[Obstacle] = field(default_factory=list)

    def is_obstacle(self, x, y):
        for obs in self.list_obstacles:
            if obs.x == x and obs.y == y:
                return True
        return False

def create_world(list_of_positions):
    obstacles = []
    for pos in list_of_positions:
        obstacles.append(Obstacle(pos[0], pos[1]))
    world = World(obstacles)
    return world
