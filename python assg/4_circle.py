# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

class circle():

    def __init__(self,r):
        self.radius=r
    
    def area(self):
        # pi=3.14
        result=self.radius**2*3.14
        return result
circle_area=circle(2)
print(int(circle_area.area()))