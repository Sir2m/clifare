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
        if (type(pay) != int) or (pay < 0):
            print("You surly don't pay this.")
            self.pay = inter(input("Tell me again how much did he/she paid? "))
        else:
            self._pay = pay


    def __add__(self, other):
        try:
            return Wallet(self.pay + other.pay)
        except KeyboardInterrupt:
            quit()
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


    # the variable to set the unknown "x" name with
    UNKX = 1

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name:str):
        if (not name) or (type(name) != str):
            name = f"unknown {Person.UNKX}"
            Person.UNKX += 1
        
        self._name = name
    

    @property
    def amount(self):
        return self._amount


    @amount.setter
    def amount(self, quantity: int):
        if quantity == None:
            self._amount = 1
        elif (type(quantity) != int) or (quantity < 1):
            self.amount = inter(input("Wait what? How much again? "))
        else:
            self._amount = quantity


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
        self.change = price


    @property
    def change(self):
        return self._change


    @change.setter
    def change(self, price):
        while (not price) or (type(price) != int) or (price < 0):
            price = inter(input('What a price! was that a sample??\nwhat was the price? '))
        x = self.pay - self.amount * price
        if x < 0:
            print("You are will be in Debt")
            self.pay = inter(input("How much did he pay you told me? "))
            self.amount = inter(input("And you told me how much? "))
            self.change = inter(input("Finally, what was the price? "))
        else:
            self._change = x


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
        item = item.title()
        try:
            # int used not inter since this method is by design made
            # to catch the error not to deal with it 
            price = int(input(f"Price of {item}? "))
            if price > 0:
                cls.MENU[item] = price
            else:
                raise ValueError
        except KeyboardInterrupt:
            quit()
        except:
            print('You guys pay this?\nagain')
            cls.add_item(item)


    def add_order(self, item:str, quantity:int):
        item = item.title()
        self.amount = quantity
        if item not in Menue.MENU:
            Menue.add_item(item)
        if item in self.order:
            self.order[item] += self.amount
        else:
            self.order[item] = self.amount


def inter(inp):
    """
    since none integer values are already handled, and at the same
    time the setters do not cast by themselves the inputs, this
    function is vital
    """
    try:
        return int(inp)
    except KeyboardInterrupt:
        quit()
    except:
        return inp