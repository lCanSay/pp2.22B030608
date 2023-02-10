class Point():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(str(self.x)+ " " + str(self.y))
    def move(self):
        x = int(input())
        y = int(input())
        self.x = x
        self.y = y
    def dist(self):
        print(abs(self.x-self.y))

a = Point(1,3)

a.move()
a.show()
a.dist()