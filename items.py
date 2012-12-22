class Item(object):
    names = set()
    
    def __init__(self):
        super(Item, self).__init__()
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


class Container(object):

    def __init__(self):
        super(Container, self).__init__()
        self.items = {}
        self.is_open = False

    def add_item(self, item):
        for name in item.names:
            self.items[name] = item

    def get(self, name):
        if not self.is_open:
            return None
        else:
            return self.items.get(name)
