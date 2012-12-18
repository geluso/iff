#!/usr/local/bin/python3

import code

class Direction(object):
  directions = {}
  def __init__(self, name):
    self.name = name
    Direction.directions[name] = self

  def __str__(self):
    return self.name

  @classmethod
  def str_to_dir(cls, str):
    return cls.directions[str]

Direction.NORTH = Direction("north")
Direction.SOUTH = Direction("south")
Direction.EAST = Direction("east")
Direction.WEST = Direction("west")

class Room(object):
  def __init__(self, title, description):
    self.title = title
    self.description = description 
    self.exits = {}

  def add_exit(self, direction, room):
    self.exits[direction] = room

  def __str__(self):
    return "%s\n%s\n%s\n" % (self.title, (len(self.title) * "="), self.description)

class Universe(object):
  def __init__(self, start_room):
    self.current_room = start_room

  def move(self, direction):
    direction = Direction.str_to_dir(direction)
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]

  def accept_input(self):
    return code.InteractiveConsole.raw_input("? ")

  def tick(self):
    print(self.current_room)
    input = self.accept_input()
    print()
    self.move(input)

kitchen = Room("The Kitchen", "You are in the kitchen. The lights are off. There is a hall south.")
pantry = Room("The Pantry", "You stumble through the darkness and trip over a stale loaf of bread. As you fall you grab for something to stable yourself. Your hand falls on the stovetop and is burnt. In a panic you knock over a rack of knives and they soar into the air before plunging into your back. They puncture your lungs. In your last moments, you cut yourself a slice of bread.")
kitchen.add_exit(Direction.EAST, pantry)
universe = Universe(kitchen)
while(True):
  universe.tick()
