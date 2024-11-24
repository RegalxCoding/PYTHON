from abc import ABC,abstractmethod
class Friend(ABC):
    @abstractmethod
    def role(self):
        pass
    def show(self):
        print("concrete method")
class girlfriend(Friend):
    def role(self):
        print("gf")
g=girlfriend()
g.show()
g.role()

#@abstract property
from abc import ABC,property
class Hero(ABC):
    @property
    def HeroName(self):
        return self.Hname
class Insta(Hero):
    def __init__(self):
        self.Hname="Rushabh"
i=Insta()
print("HERO NAME:",i.Hname)