class Area():
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def square(self):
        return self.l * self.b

class Square():
    def __init__(self, r):
        super.__init__(r, r)
