__str2dir__ = {}

class Direction(object):
  def __init__(self, name):
    self.name = name
    __str2dir__[name] = self

  def __str__(self):
    return self.name


def str_to_dir(string):
    return __str2dir__[string]

def valid_movement(string):
    return "go" in string.split(" ")

NORTH = Direction("north")
SOUTH = Direction("south")
EAST = Direction("east")
WEST = Direction("west")
