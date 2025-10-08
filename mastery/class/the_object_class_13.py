# class Animal:
#     def __init__(self):
#         self.age = 1
#
#     def eat(self):
#         print("eat")
#
# class Mammals(Animal):
#     def walk(self):
#         print("eat")
# class Fish(Mammals):
#     def swim(self):
#         print("swim")
#
# mammals = Mammals()
# # print(Mammals.eat())
#
# print(isinstance(mammals, Mammals))
# print(isinstance(mammals, Animal))



class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class Mammals(Animal):
    def walk(self):
        print("eat")
class Fish(Mammals):
    def swim(self):
        print("swim")

mammals = Mammals()
# print(Mammals.eat())

print(isinstance(mammals, object))
print(isinstance(mammals, Fish))
