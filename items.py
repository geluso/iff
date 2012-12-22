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
