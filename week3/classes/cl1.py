class first():
    def getString(self):
        self.input = str(input("Enter your string\n"))
    def printString(self):
        print((self.input).upper())

a = first()
a.getString()
a.printString()