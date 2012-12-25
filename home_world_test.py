#!/usr/local/bin/python3

import unittest

import universe

import home_world

class Test(unittest.TestCase):

  def setUp(self):
    self.universe = universe.MockUniverse(home_world.living_room)

  def verify_has_output(self):
    self.assertTrue(self.universe.output.last_output)

  def verify_output(self, expected_string):
    self.assertEqual(self.universe.output.last_output, expected_string)
    
  def test_open_close_box(self):
    self.universe.tick("look box")
    self.verify_has_output()
    self.universe.tick("look book")
    self.verify_output("There is no book here.")
    self.universe.tick("open box")
    self.verify_has_output()
    self.universe.tick("look book")
    self.verify_output("A book titled 'Ithkuil: A Philosophical Design for "
                       "a Hypothetical Language'")

  def test_go_nonexit(self):
    self.universe.tick("go west")
    self.verify_output("I can't go west.")


if __name__ == '__main__':
  unittest.main()
