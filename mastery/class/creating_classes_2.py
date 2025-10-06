
class Point:
    def draw(self):
        print("Draw")

point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))