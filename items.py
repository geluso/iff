class Item(object):
  def __init__(self):
    self.reactions = {}

  def __str__(self):
      return "%s" % self.description
    
  def do(self, action):
    if action in self.reactions:
      self.reactions[action]()
    else:
      self.nothing()

  def add_action(self, action):
      self.reactions[action.__name__] = action

  def nothing(self):
    print("it does nothing.")


