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
        self.add_action(self.open)

    def open(self):
        self.is_open = True
        print("You open the box.")


class Bread(items.Item):
  def __init__(self):
    super(Bread, self).__init__()
    self.add_action(self.eat)

  def eat(self):
    print("You eat the loaf of bread.")


# Define rooms

class Kitchen(rooms.Room):

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


class LivingRoom(rooms.Room):

    title = "Living Room"
    description = "You are in a living room. There isn't much here. On the " \
        "floor is a box. In a corner is an aquarium. To the north is a kitchen."

    def __init__(self):
        super(LivingRoom, self).__init__()
        self.add_items([Box()])


class Pantry(rooms.Room):

  title = "The Pantry"
  description = "You stumble through the darkness and trip over a stale loaf of " \
      "bread. As you fall you grab for something to stable yourself. Your hand falls " \
      "on the stovetop and is burnt. In a panic you knock over a rack of knives and " \
      "they soar into the air before plunging into your back. They puncture your " \
      "lungs. In your last moments, you cut yourself a slice of bread."

# Connect rooms

living_room = LivingRoom()
kitchen = Kitchen()
pantry = Pantry()
rooms.connect(living_room, kitchen, directions.NORTH)
rooms.connect(kitchen, pantry, directions.EAST)
