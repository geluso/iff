#!/usr/local/bin/python3

import room
from collections import defaultdict

class Direction(object):
  directions = defaultdict()
  def __init__(self, name):
    self.name = name
    Direction.directions[name] = self

  def __str__(self):
    return self.name

  @classmethod
  def str_to_dir(cls, str):
    return cls.directions[str]

  @classmethod
  def valid_movement(cls, str):
    return "go" in str.split(" ")

Direction.NORTH = Direction("north")
Direction.SOUTH = Direction("south")
Direction.EAST = Direction("east")
Direction.WEST = Direction("west")

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
    direction = Direction.str_to_dir(direction)
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]

  def accept_input(self):
    return input("? ")


  def tick(self):
    print(self.current_room)
    input = self.accept_input()
    print()
    if Direction.valid_movement(input):
      direction = input.split(" ")[1]
      self.move(direction)
    else:
      print("I don't know how to %s.\n" % input)

kitchen = room.Kitchen()
pantry = room.Pantry()
kitchen.add_exit(Direction.EAST, pantry)
universe = Universe(kitchen)
while(True):
  universe.tick()
