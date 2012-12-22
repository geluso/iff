import directions
import items
import rooms

# Define items
class Box(items.Item):

    names = set(["box"])
    description = "A brown cardboard box."

    def __init__(self):
        super(Box, self).__init__()
        self.is_open = False
        self.reactions["open"] = self.open

    def open(self):
        self.is_open = True
        print("You open the box.")


class Bread(items.Item):
  def __init__(self):
    super(Bread, self).__init__()
    self.reactions["eat"] = self.eat 

  def eat(self):
    print("You eat the loaf of bread.")


# Define rooms

class Kitchen(rooms.Room):

  title = "The Kitchen"

  def __init__(self):
    super(Kitchen, self).__init__() 
    self.light_is_on = False
    self.box = Box()
    for name in self.box.names:
        self.items[name] = self.box

  @property
  def description(self):
    return "You are in the kitchen. " + self.light() + " There is a pantry east."

  def light(self):
    if self.light_is_on:
      return "The room is brightly lit. You see a candlestick."
    else:
      return "The lights are off."


class Pantry(rooms.Room):

  title = "The Pantry"
  description = "You stumble through the darkness and trip over a stale loaf of " \
      "bread. As you fall you grab for something to stable yourself. Your hand falls " \
      "on the stovetop and is burnt. In a panic you knock over a rack of knives and " \
      "they soar into the air before plunging into your back. They puncture your " \
      "lungs. In your last moments, you cut yourself a slice of bread."

# Connect rooms

kitchen = Kitchen()
pantry = Pantry()
rooms.connect(kitchen, pantry, directions.EAST)
