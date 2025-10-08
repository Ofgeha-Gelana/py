class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = Account("Ofgeha", 100)
print(account.get_balance())

try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error: {e}")

print(account._Account__balance)