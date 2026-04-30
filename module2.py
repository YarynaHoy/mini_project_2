# module 2 assientment 1

# 1
class Bike:
    def __init__(self, s, f):
        self.color = s
        self.price = f

testOne = Bike('blue', 89.99)
testTwo = Bike('purple', 25.0)

# 2
class AppleBasket:
    def __init__(self,s ,n):
        self.apple_color = s
        self.apple_quantity = n

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."


b1 = AppleBasket('red', 4)
assert str(b1) == "A basket of 4 red apples."

# 3
class BankAccount:
    def __init__(self, name, i):
        self.__name = name
        self.__atm = i

    def __str__(self):
        return f"Your account, {self.__name}, has {self.__atm} dollars."

t1 = BankAccount('Bob', 100)
