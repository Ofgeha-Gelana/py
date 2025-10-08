# class Product:
#     def __init__(self, price):
#         self.set_price(price)
#
#     def get_price(self):
#         return self.__price
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("Value cannot be negative")
#         self.__price = value
#
# product = Product(100)
# print(product.get_price())
#
# product.set_price(200)
# print(product.get_price())



# The above code will be written as java programmer learning to write a python
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__price = value

product = Product(100)
print(product.price)
