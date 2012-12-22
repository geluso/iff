class CommandParser(object):

  def __init__(self, universe):
    self.universe = universe

  def exec(self, user_input):
    tokens = user_input.split(" ")
    command = tokens[0]
    args = tokens[1:]
    if command == "go":
        self.do_go(command, args)
    elif command == "look":
        self.do_look(command, args)
    else:
      success = self.do_item_action(command, args)
      if not success:
        print("I don't know how to %s.\n" % user_input)

  def do_go(self, command, args):
      if len(args) == 1:
          self.universe.move(args[0])
      else:
          print("I can only go in one direction at a time.")

  def do_look(self, command, args):
      # If no args look at current room
      if not args:
        self.universe.look()
      # else if single arg look at arg
      elif len(args) == 1:
        item = self.universe.current_room.items.get(args[0])
        if item:
          print(item)
      else:
          print("I don't know what to look at.")

  def do_item_action(self, command, args):
      if len(args) == 1:
          # Search through current items in the room
          item = self.universe.current_room.items.get(args[0])
          if item and command in item.reactions:
              item.do(command)
              return True
          # Search through current containers in the room
          for item in self.universe.current_room.items.values():
              if hasattr(item, "get"):
                  target = item.get(args[0])
                  if target and command in target.reactions:
                      target.do(command)
                      return True
      return False
