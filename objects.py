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
    def amount(self, quantity: int | None = None):
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
        self.price = price
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


    def change_pay(self, pay):
        self.pay = pay
        self.change = self.price
        print("\nPrice changed successfully")


    def change_amount(self, amount):
        self.amount = amount
        self.change = self.price
        print("\nAmount changed successfully")

    def __str__(self):
        return f"Name: {self.name}\nPaid: {self.pay}\nFor: {self.amount}\nChange: {self.change}\nPrice: {self.price}"


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
    TAX = 0

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


    # will be needed for better testings
    @classmethod
    def del_menu(cls):
        cls.MENU = {}


    @classmethod
    def edit_price(cls):
        cls.print_menu()
        inp = input("Which item you wanna change? ")
        inp = inp.title()
        if pri := cls.MENU.get(inp):
            print(f"Current price = {pri}")
            pri = getter('New price: ', True,
                         lambda x: x > 0,
                         "\nNew Price is set!\n")


    @classmethod
    def print_menu(cls):
        print()
        for k, v in cls.MENU.items():
            print(f"{k} for {v}")
        print()


    @classmethod
    def add_tax(cls):
        inp = getter("Enter price (0.x): ", True,
                     lambda x: 1 > x > 0,
                     '\nTax is set successfully!\n')

    
    def add_order(self, item:str, quantity:int):
        item = item.title()
        self.amount = quantity
        if not item:
            print("Wrong name!\n")
        if item not in Menue.MENU:
            Menue.add_item(item)
        if item in self.order:
            self.order[item] += self.amount
        else:
            self.order[item] = self.amount
        self.amount = None

    
    def to_pay(self):
        self.get_cost()
        self.pay = inter(input("Pay: "))
        if self.pay >= self.cost:
            print('\nYou Paid Successfully!\n')
            self.get_change()
        else:
            print("\nCheck cost and pay again!\n")

    def get_change(self):
        self.change = self.pay - self.cost
        if self.change < 1:
            raise ValueError

    def get_cost(self):
        total = 0
        try:
            for dish, amount in self.order.items():
                total += amount * self.MENU[dish]
        except KeyboardInterrupt:
            quit()
        except:
            print("Something is wrong, delete this object")
        self.cost = total * (1 + self.TAX)


    def __str__(self):
        name = f"Name: {self.name}\n"
        order = "Order:\n"
        for k, v in self.order.items():
            order += f"       {v} of {k}\n"
        return name + order
        


class Payers:
    def __init__(self):
        self.list = []
        # match mode.__qualname__:
        #     case Farer.__qualname__:
        #         pass
        #     case Menue.__qualname__:
        #         pass


    def add(self, obj):
        if obj:
            self.list.append(obj)


    def money(self):
        x = Wallet(0)
        for i in self.list:
            x += i
        return x.pay
    

    def change(self):
        for i in self.list:
            # the paid amount is written for removing any conflict may be done with nameless objects
            print(f"{i.name}, paid {i.pay}, change is  {i.change}")
    

    def show(self):
        print('people in list: ')
        for i in self.list:
            print(i.name)
    

    def order(self, ext: bool = False):
        cash = Wallet(0)
        order = {}
        for i in self.list:
            for k,v in i.order.items():
                if k in order:
                    order[k] += v
                else:
                    order[k] = v
            if ext:
                print(i)
            print(f"{i.name} change is {i.change}")
            cash += i
        print("Full order:")
        for n, m in order.items():
            print(f"           {m} of {n}")


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


def getter(msg:str, set_stat:bool = False, bool_cond = None, set_msg: str | None = None):
    """
    made mainly to get the no wanted to choose mode, also will
    be used in the normal Fare mode since price will be set
    once and this will save a lot of time later 
    """
    while True:
        try:
            x = int(input(msg))
        except KeyboardInterrupt:
            quit()
        except:
            continue
        if set_stat:
            if bool_cond(x):
                if set_msg:
                    print(set_msg)
            else:
                continue
        return x