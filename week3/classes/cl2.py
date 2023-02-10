class Shape():
    def area(self):
        print(self.area)
    class Square():
        def __init__(self, length):
            self.area = 0
            self.length = length
            self.area = length *length
        def area(self):
            print(self.area)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        self.area = 0
        self.area = length * width
    def area(self):
        print(self.area)



baza = Shape.Square(13)
print(baza.area)


rec = Rectangle(3,4)
print(rec.area)