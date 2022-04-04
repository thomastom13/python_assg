# 5.Define a class named Rectangle which can be constructed by a length and width.
#  The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area_rect(self):
        result = self.length*self.width
        return result
rect=Rectangle(3,3)
print(rect.area_rect())
