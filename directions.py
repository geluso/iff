__str2dir__ = {}
__opposites__ = {}

class Direction(object):
  def __init__(self, name):
    self.name = name
    __str2dir__[name] = self

  def __str__(self):
    return self.name

  def opposite(self):
      return __opposites__[self]


def str_to_dir(string):
    return __str2dir__[string]

def valid_movement(string):
    return "go" in string.split(" ")

NORTH = Direction("north")
SOUTH = Direction("south")
EAST = Direction("east")
WEST = Direction("west")

__opposites__[NORTH] = SOUTH
__opposites__[SOUTH] = NORTH
__opposites__[EAST] = WEST
__opposites__[WEST] = EAST
