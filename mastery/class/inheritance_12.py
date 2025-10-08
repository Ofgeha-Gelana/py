# # The following is duplicated as you can see from the following
# class Mammals:
#     def eat(self):
#         print("Mammal.eat")
#     def walk(self):
#         print("Mammal.walk")
#
# class Fish:
#     def eat(self):
#         print("Mammal.eat")
#     def walk(self):
#         print("Mammal.walk")


# The following is pythonic
class Animal:
    def eat(self):
        print("eat")

class Mammals(Animal):
    def walk(self):
        print("eat")
class Fish(Mammals):
    def swim(self):
        print("swim")

Mammals = Mammals()
print(Mammals.eat())
