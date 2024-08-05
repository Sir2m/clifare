class Wallet:
    def __init__(self, pay:int):
        self.pay = pay

    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, pay:int):
        if type(pay) != int:
            raise ValueError("You surly don't pay this.")
        
        self._pay = pay

    def __add__(self, other):
        return Wallet(self.pay + other.pay)


class Person(Wallet):
    def __init__(self, name:str, pay:int):
        super().__init__(pay)
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name:str):
        if not name:
            global unkx
            name = f"unknown {unkx}"
            unkx += 1
        
        self._name = name


class Farer(Person):
    def __init__(self, name:str, pay:int, price:int, quantity:int|None):
        super().__init__(name, pay)
        self.amount = quantity
        self.charge = self.pay - self.amount * price
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def quantity(self, quantity):
        if quantity == None:
            quantity = 1
        self._amount = quantity


class Menue(Person):
    def __init__(self, name: str):
        super().__init__(name, 0)
        self.order = {}

    menu = {}

    @classmethod
    def add_item(cls, item:str, price:int):
        cls.menu[item] = price

    def add_order(self, item, quantity):
        if item not in Menue.menu:
            price = int(input(f"price of {item}?"))
            Menue.add_item(item, price)
        if item in self.order:
            self.order[item] += quantity
        else:
            self.order[item] = quantity
unkx = 1