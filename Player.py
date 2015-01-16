__author__ = 'Kot'
from Entity import Entity


class Player(Entity):
    def __init__(self, name, x, y, keylist):
        Entity.__init__(self, name, x, y, keylist)

    def update(self):
        if self.keylist[ord('w')] == True:
            self.y -= 1
        elif self.keylist[ord('s')] == True:
            self.y += 1
        elif self.keylist[ord('d')] == True:
            self.x += 1
        elif self.keylist[ord('a')] == True:
            self.x -= 1

    def render(self):
        #TODO: DO THIS :)
        return
