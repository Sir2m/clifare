class Wallet:
    """
    This class is the standard class for any summation between
    the other classes

    this was not included in the 'Person' class since addition
    does not need for a 'name' parameter which is a part in
    'Person' class
    """
    def __init__(self, pay:int):
        """
        initializing the class

        :param 'pay': the amount of paid money that will be summed
        :param type: int 
        """
        self.pay = pay


    @property
    def pay(self):
        return self._pay


    @pay.setter
    def pay(self, pay:int):
        if (type(pay) != int) | (pay < 0):
            print("You surly don't pay this.")
            self.pay = input("Tell me again how much did he/she paid? ")
        else:
            self._pay = pay


    def __add__(self, other):
        try:
            return Wallet(self.pay + other.pay)
        except:
            raise Exception("Code Error")


class Person(Wallet):
    """
    the main interface set for the to be used classes
    """
    def __init__(self, name:str, pay:int):
        """
        initializing the class

        :param 'name': the name of the payer
        :param type: str or None

        :param 'pay': the amount of paid money that will be summed
        :param type: int 
        """
        super().__init__(pay)
        self.name = name


    # the variable to set the unknow "x" name with
    UNKX = 1

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name:str):
        if (not name) | (type(name) != str):
            name = f"unknown {Person.UNKX}"
            Person.UNKX += 1
        
        self._name = name


class Farer(Person):
    """
    This class is used for the simple calculations for the fare modes
    """
    def __init__(self, name:str, pay:int, price:int, quantity:int):
        """
        initializing the class

        :param 'name': the name of the payer
        :param type: str or None

        :param 'pay': the amount of paid money that will be summed
        :param type: int

        :param 'price': the price of the unit of thing to pay for
        :param type: int

        :param 'quantity': the amount that person payed for
        :param type: int
        """
        super().__init__(name, pay)
        self.amount = quantity
        self.charge = price


    @property
    def charge(self):
        return self._charge


    @charge.setter
    def charge(self, price):
        x = self.pay - self.amount * price
        if x < 0:
            print("You are will be in Debt")
            self.pay = int(input("How much did he pay you told me? "))
            self.amount = int(input("And you told me how much?"))
            self.charge = int(input("Finally, what was the price?"))
        else:
            self._charge = x


    @property
    def amount(self):
        return self._amount


    @amount.setter
    def amount(self, quantity: int):
        if quantity == None:
            quantity = 1
        elif type(quantity) != int:
            self.amount = int(input("Wait what? How much again?"))
        else:
            self._amount = quantity


class Menue(Person):
    """
    This class is made for the Restaurant mode, it made to work assist with the complexity of
    ordering for a group
    """
    def __init__(self, name: str):
        """
        initializing the class

        :param 'name': the name of the payer
        :param type: str or None
        """
        # paying is a matter of later time
        super().__init__(name, 0)
        self.order = {}

    # the place to store the price of all kinds ordered in the order
    MENU = {}

    @classmethod
    def add_item(cls, item:str):
        try:
            price = int(input(f"Price of {item}? "))
            cls.MENU[item] = price
        except:
            print('You guys pay this?\nagain')
            cls.add_item(item)


    def add_order(self, item:str, quantity:int):
        if item.capitalize() not in Menue.MENU:
            Menue.add_item(item)
        if item in self.order:
            self.order[item] += quantity
        else:
            self.order[item] = quantity
