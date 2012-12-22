#!/usr/local/bin/python3

from collections import defaultdict

import rooms
import directions
import home_world


class Universe(object):
  def __init__(self, start_room):
    self.current_room = start_room
    self.command_parser = CommandParser(self)
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
      print("I don't know how to %s.\n" % input)


universe = Universe(home_world.kitchen)
while(True):
  universe.tick()
