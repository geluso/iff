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


universe = Universe(home_world.living_room)
while(True):
  universe.tick()
