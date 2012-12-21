import directions

class Room(object):

  title = "No Title"
  description = "It's dark."

  def __init__(self):
    self.exits = {}

  def __str__(self):
    return "%s\n%s\n%s\n" % (self.title, (len(self.title) * "="), self.description)

def connect(src, dest, direction, bidirectional=True):
  src.exits[direction] = dest
  if bidirectional:
    dest.exits[direction.opposite()] = src


class Kitchen(Room):

  title = "The Kitchen"

  def __init__(self):
    super(Kitchen, self).__init__() 
    self.light_is_on = False

  @property
  def description(self):
    return "You are in the kitchen. " + self.light() + " There is a pantry east."

  def light(self):
    if self.light_is_on:
      return "The room is brightly lit. You see a candlestick."
    else:
      return "The lights are off."


class Pantry(Room):

  title = "The Pantry"
  description = "You stumble through the darkness and trip over a stale loaf of " \
      "bread. As you fall you grab for something to stable yourself. Your hand falls " \
      "on the stovetop and is burnt. In a panic you knock over a rack of knives and " \
      "they soar into the air before plunging into your back. They puncture your " \
      "lungs. In your last moments, you cut yourself a slice of bread."
