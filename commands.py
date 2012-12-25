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
    elif command == "inventory":
      self.do_look_at_inventory()
    elif command == "get":
      self.do_get(command, args)
    elif command == "drop":
      self.do_drop(command, args)
    else:
      success = self.do_item_action(command, args)
      if not success:
        print("I don't know how to %s.\n" % user_input)

  def do_go(self, command, args):
      if len(args) == 1:
          self.universe.move(args[0])
      else:
          self.universe.print("I can only go in one direction at a time.")

  def do_look(self, command, args):
      # If no args look at current room
      if not args:
        self.universe.look()
      # else if single arg look at arg
      elif len(args) == 1:
        item = self.universe.visible_items.get(args[0])
        if item:
          self.universe.print(item)
        else:
            self.universe.print("There is no %s here." % args[0])
      else:
          self.universe.print("I don't know what to look at.")

  def do_look_at_inventory(self):
    self.universe.look_at_inventory()

  def do_get(self, command, args):
    if args[0] in self.universe.current_room.items:
      item = self.universe.current_room.items[args[0]]
      self.universe.add_to_inventory(item)
      del self.universe.current_room.items[args[0]]
      self.universe.print("You pick up the %s." % args[0])
    else:
      self.universe.print("I don't see any %s here." % args[0])

  def do_drop(self, command, args):
    print(args[0])
    for item in self.universe.inventory:
      if args[0] in item.names:
        self.universe.remove_from_inventory(item)
        self.universe.current_room.add_items([item])
        self.universe.print("You drop the %s." % args[0])
        break
    else:
      self.universe.print("I don't see any %s here." % args[0])

  def do_item_action(self, command, args):
      if len(args) == 1:
          item = self.universe.visible_items.get(args[0])
          if item and command in item.reactions:
              item.do(command, self.universe)
              return True
      return False
