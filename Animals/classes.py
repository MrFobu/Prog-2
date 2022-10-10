class Animal():
    def __innit__(self, name):
        self.name = name

class Bird(Animal):
    def __innit__(self, wingspand):
        self.wingspand = wingspand

class Fish(Animal):
    def __innit__(self,max_depth):
        self.max_depth = max_depth

class Salmon(Fish):
    def __innit__(self,speed):
        self.speed = speed

class Shark(Fish):
    def __innit__(self,teeth):
        self.teeth = teeth