import commands
import directions
import rooms

class Universe(object):
  def __init__(self, start_room, output=None):
    self.inventory = []
    self.current_room = start_room
    self.visible_items = VisibleItems(self)

    self.command_parser = commands.CommandParser(self)
    if output:
      self.output = output
    else:
      self.output = StdOutput()
    self.print(self.current_room)

  def print(self, string):
    self.output.print(string)

  def move(self, direction):
    direction = directions.str_to_dir(direction)
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]
      self.print(self.current_room)
    else:
      self.print("I can't go %s." % direction)

  def look(self):
    self.print(self.current_room)

  def look_at_inventory(self):
    if not self.inventory:
      self.print("You have nothing.")
    else:
      self.print("You have:")
      for item in self.inventory:
        self.print(item)

  def add_to_inventory(self, item):
    self.inventory.append(item)

  def remove_from_inventory(self, item):
    self.inventory.remove(item)

  def accept_input(self):
    self.print("")
    user_input = input("? ")
    self.print("")
    return user_input

  def tick(self, user_input=None):
      if user_input is None:
          user_input = self.accept_input()
      self.command_parser.exec(user_input)


class MockUniverse(Universe):

  def __init__(self, start_room):
    super(MockUniverse, self).__init__(start_room, MockOutput())

class VisibleItems(object):
  """Keeps track of the visible items in the universe."""
  
  def __init__(self, universe):
    self.universe = universe

  def get(self, name):
    """Given a str name returns the item with that name if it is visible."""
    # scan through the items in inventory
    for item in self.universe.inventory:
      if name in item.names:
        return name
    # scan through items in the room
    item = self.universe.current_room.items.get(name)
    if item:
      return item
    # scan through containers in the room
    for item in self.universe.current_room.items.values():
      if hasattr(item, "get"):
        target = item.get(name)
        if target:
          return target
    return None

class StdOutput(object):

  def print(self, string):
    print(string)
    
    
class MockOutput(object):

  def __init__(self):
    self.last_output = None

  def print(self, string):
    self.last_output = str(string)
