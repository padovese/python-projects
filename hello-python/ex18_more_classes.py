##inherent
class Animale(object):
    pass

class Dinosauro(Animale):
    def __init__(self, name):
        self.name = name

class Bipede(Dinosauro):
    def roar(self):
        print "I am", self.name
        print "ROAR!"

Bipede("T-Rex").roar()


##using super to call parent constructor

class Quadrupede(Dinosauro):
    def __init__(self):
        super(Quadrupede, self).__init__("Triceratops")

    def roar(self):
        print "I am", self.name
        print "ROAR!"

Quadrupede().roar()
