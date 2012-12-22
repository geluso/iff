import directions

class Room(object):

  title = "No Title"
  description = "It's dark."

  def __init__(self):
    self.exits = {}
    self.items = {}

  def __str__(self):
    return "%s\n%s\n%s" % (self.title, (len(self.title) * "="), self.description)

  def add_items(self, items):
    for item in items:
      for name in item.names:
        self.items[name] = item

def connect(src, dest, direction, bidirectional=True):
  src.exits[direction] = dest
  if bidirectional:
    dest.exits[direction.opposite()] = src
