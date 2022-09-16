import math

class Shapes:
    def __init__(self):
        pass

class Rectangle(Shapes):
    def __init__(self,l,w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Circle(Shapes):
    def __init__(self,r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

class Triangle(Shapes):
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h / 2

with open('shapes.txt') as f:
    CCount = 0
    RCount = 0
    TCount = 0
    for line in f:
        tokens = line.split(',')
        curr = Shapes()
        if tokens[0] == 'Circle':
            CCount += 1
            curr = Circle(int(tokens[1]))
            print(f'Circle {CCount}:',curr.area())
        elif tokens[0] == 'Rectangle':
            RCount += 1
            curr = Rectangle(int(tokens[1]),int(tokens[2]))
            print(f'Rectangle {RCount}:',curr.area())
        else:
            TCount += 1
            curr = Triangle(int(tokens[1]),int(tokens[2]))
            print(f'Triangle {TCount}:',curr.area())
