#!/usr/local/bin/python3

from collections import defaultdict

import commands
import directions
import rooms

import home_world

class Universe(object):
  def __init__(self, start_room):
    self.current_room = start_room
    self.command_parser = commands.CommandParser(self)
    self.visible_items = VisibleItems(self)
    print(self.current_room)

  def move(self, direction):
    direction = directions.str_to_dir(direction)
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]
      print(self.current_room)

  def look(self):
    print(self.current_room)

  def accept_input(self):
    print()
    user_input = input("? ")
    print()
    return user_input

  def tick(self):
    user_input = self.accept_input()
    self.command_parser.exec(user_input)


class VisibleItems(object):
    """Keeps track of the visible items in the universe."""

    def __init__(self, universe):
        self.universe = universe

    def get(self, name):
        """Given a str name returns the item with that name if it is visible."""
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


universe = Universe(home_world.living_room)
while(True):
  universe.tick()
