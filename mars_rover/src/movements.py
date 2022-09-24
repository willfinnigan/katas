def move_north(x, y):
    y += 1
    if y == 10:
        y = 0
    return x, y

def move_east(x, y):
    x += 1
    if x == 10:
        x = 0
    return x, y

def move_south(x, y):
    y -= 1
    if y == -1:
        y = 9
    return x, y

def move_west(x, y):
    x -= 1
    if x == -1:
        x = 9
    return x, y



