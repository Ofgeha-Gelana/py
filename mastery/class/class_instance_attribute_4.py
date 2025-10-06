class Point:
    default_color = "Red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        return f"Point({self.x}, {self.y})"

Point.default_color = "Green"
point = Point(1,2)
print(point.draw())
print(point.default_color)

another = Point(3,4)
print(another.draw())
print(another.default_color)