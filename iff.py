#!/usr/local/bin/python3

from collections import defaultdict

import rooms
import directions


class Item(object):
  def __init__(self):
    self.reactions = {}
    
  def do(self, action):
    if action in self.reactions:
      self.reactions[action]()
    else:
      self.nothing()

  def nothing(self):
    print("it does nothing.")

class Bread(Item):
  def __init__(self):
    super(Bread, self).__init__()
    self.reactions["eat"] = self.eat 

  def eat(self):
    print("You eat the loaf of bread.")

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
      self.universe.look()
    else:
      print("I don't know how to %s.\n" % input)


kitchen = rooms.Kitchen()
pantry = rooms.Pantry()
rooms.connect(kitchen, pantry, directions.EAST)

universe = Universe(kitchen)
while(True):
  universe.tick()
