import directions
import rooms

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
