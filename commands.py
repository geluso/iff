class CommandParser(object):

  def __init__(self, universe):
    self.universe = universe

  def exec(self, user_input):
    tokens = user_input.split(" ")
    command = tokens[0]
    args = tokens[1:]
    if command == "go":
      if len(args) == 1:
        self.universe.move(args[0])
      else:
        print("I can only go in one direction at a time.")
    elif command == "look":
      # If no args look at current room
      if not args:
        self.universe.look()
      # else if single arg look at arg
      elif len(args) == 1:
        item = self.universe.current_room.items.get(args[0])
        if item:
          print(item)
    else:
      failure = True
      if len(args) == 1:
        item = self.universe.current_room.items.get(args[0])
        if item and command in item.reactions:
          item.do(command)
          failure = False
      if failure:
        print("I don't know how to %s.\n" % input)
