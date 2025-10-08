# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# print(p1 == p2)


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p1 = Point(3, 4)
p2 = Point(5, 6)
print(p1.x, p1.y)

