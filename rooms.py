import directions

class Room(object):

  title = "No Title"
  description = "It's dark."

  def __init__(self):
    self.exits = {}

  def __str__(self):
    return "%s\n%s\n%s" % (self.title, (len(self.title) * "="), self.description)

def connect(src, dest, direction, bidirectional=True):
  src.exits[direction] = dest
  if bidirectional:
    dest.exits[direction.opposite()] = src
