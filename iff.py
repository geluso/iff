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

  def move(self, direction):
    direction = directions.str_to_dir(direction)
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]

  def accept_input(self):
    return input("? ")


  def tick(self):
    print(self.current_room)
    input = self.accept_input()
    print()
    if directions.valid_movement(input):
      direction = input.split(" ")[1]
      self.move(direction)
    else:
      print("I don't know how to %s.\n" % input)

kitchen = rooms.Kitchen()
pantry = rooms.Pantry()
rooms.connect(kitchen, pantry, directions.EAST)

universe = Universe(kitchen)
while(True):
  universe.tick()
