class Shape():
    def area(self):
        print(self.s)
    class Square():
        def __init__(self, length):
            self.s = 0
            self.length = length
            self.s = length *length
        def area(self):
            print(self.s)


class Rectangle(Shape.Square):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        self.s = 0
        self.s = length * width
    def area(self):
        print(self.s)



baza = Shape.Square(13)
baza.area()


rec = Rectangle(3,4)
rec.area()