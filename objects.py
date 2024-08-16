class Wallet:
    """
    This class is the standard class for any summation between
    the other classes

    this was not included in the 'Person' class since addition
    does not need for a 'name' parameter which is a part in
    'Person' class
    
    it includes the setter of pay with the add overloading
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
        """
        It sets the pay amount in its general form (before
        checking cost) it handles non integer or non positive
        values
        """
        if ((type(pay) != int) and (type(pay) != float)) or (pay < 0):
            print("You surly don't pay this.")
            self.pay = inter(input("Tell me again how much did he/she paid? "))
        else:
            self._pay = pay


    def __add__(self, other):
        """
        calculating the full money in hand is important,
        this overloading will make it happen easily
        """
        try:
            return Wallet(self.pay + other.pay)
        except KeyboardInterrupt:
            quit()
        except:
            raise Exception("Code Error")


class Person(Wallet):
    """
    the main interface set for the to be used classes, made to
    include all what is needed 'the same way' with the two classes

    it inherit from Wallet class to get the pay setter and add
    overloading

    it includes the setter of name, the setter of amount and a
    class variable UNKX
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


    # the variable to set the UNKnown "X" name with
    UNKX = 1

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name:str):
        """
        Sets the name given to it, and sets a name anyway to
        unknown x where x is set by the class variable UNKX
        """
        if (not name) or (type(name) != str):
            name = f"unknown {Person.UNKX}"
            Person.UNKX += 1
        
        self._name = name


    @property
    def amount(self):
        return self._amount


    @amount.setter
    def amount(self, quantity: int | None = None):
        """
        sets the amount of the paid to item, it's set to default
        of 1 when missing an input but recursively deal with bad
        inputs

        its set in the interface since setting a suitable amount
        is vital wether in fare mode or in menu mode
        """
        if quantity == None:
            self._amount = 1
        elif (type(quantity) != int) or (quantity < 1):
            self.amount = inter(input("Wait what? How much again? "))
        else:
            self._amount = quantity


class Farer(Person):
    """
    The class is made for Fare and multi Fare modes payers, it's
    set give enough flexibility to users when dealing with the
    payer, in setting, editing and showing the different attributes

    it inherit from Person, the son of Wallet

    it includes change setter, change_pay and change_amount methods
    and str overloading
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
        """
        it set the change of the person based on the price and
        quantity of the fare, it handles the problems with price
        value, all non positive values and check wether the paid
        amount is enough or not, if not it takes the responsibility
        of getting set the three values, price - quantity - pay, to
        until having a non negative change 
        """
        self.price = price
        while (not price) or ((type(price) != float) and (type(price) != int)) or (price < 0):
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
        """
        to give the flexibility to the program with keeping the set
        conditions in considerations the method was made and update
        the change
        """
        self.pay = pay
        self.change = self.price
        print("\nPrice changed successfully")


    def change_amount(self, amount):
        """
        to give the flexibility to the program with keeping the set
        conditions in considerations the method was made and update
        the change
        """
        self.amount = amount
        self.change = self.price
        print("\nAmount changed successfully")


    def __str__(self):
        """
        for easy access to the whole data in a line of code, the
        f-string is set to show all the data in the object
        """
        return f"Name: {self.name}\nPaid: {self.pay}\nFor: {self.amount}\nChange: {self.change}\nPrice: {self.price}"


class Menue(Person):
    """
    This class is made for the Menu mode, it set to deal with the
    complexity needed in the mode with less flexibility when
    compared to Farer class

    it inherits from Person, the son of Wallet

    it includes add_order, get_cost, get_change and to_pay methods
    with del_menu, add_item, add_tax, print_menu and edit_price
    class methods with MENU and TAX class attributes and str
    overloading
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
    # for non pre-set tax prices
    TAX = 0

    @classmethod
    def add_item(cls, item:str):
        """
        this method is set to add an item in the menu class
        variable putting in consideration only positive values of
        price, and checks if item is exist in first place or not
        """

        item = item.title()
        
        if item in cls.MENU:
            print('Already exists\nchange price not add item!\n')
            return
        
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


    @classmethod
    def del_menu(cls):
        """ method made mainly for tests and it resets the menu """
        cls.MENU = {}


    @classmethod
    def edit_price(cls):
        """
        this method is made for editing a price of an existing dish
        in the MENU class attribute, it handles non positive values
        """

        cls.print_menu()
        inp = input("Which item you wanna change? ")
        inp = inp.title()
        if pri := cls.MENU.get(inp):
            print(f"Current price = {pri}")
            pri = getter('New price: ', True,
                         lambda x: x > 0,
                         "\nNew Price is set!\n")
            cls.MENU[inp] = pri


    @classmethod
    def print_menu(cls):
        """ prints the whole menu with prices """

        print()
        for k, v in cls.MENU.items():
            print(f"{k} for {v}")
        print()


    @classmethod
    def add_tax(cls):
        """
        this method made for setting up a tax increase in the
        calculations, handles non float or out of range values
        """

        inp = getter("Enter percent (0.x): ", True,
                     lambda x: 1 > x >= 0,
                     '\nTax is set successfully!\n')
        cls.TAX = inp

    
    def add_order(self, item:str, quantity:int):
        """
        this method is responsible for adding instance order items
        with its quantities, it handles dishes not present in the
        menu, and already existed orders (add up at this case)
        """

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
        """
        before you pay usually, you know first what to order and how does it cost, since that the to_pay method is made and it wasn't in the initializing of the instance and it automatically checks the cost and change to validate the paid amount
        """

        self.get_cost()
        self.pay = inter(input("Pay: "))
        if self.pay >= self.cost:
            print('\nYou Paid Successfully!\n')
            self.get_change()
        else:
            print("\nCheck cost and pay again!\n")


    def get_change(self):
        """
        this method calculates the change and sets, only when to_pay is
        called at least once, it is also called inside to_pay
        """
        if self.pay:
            self.change = self.pay - self.cost
            if self.change < 1:
                raise ValueError


    def get_cost(self):
        """
        since the Menue class is more complicated, cost of the
        order differ after adding new items, and to update the cost
        calculation whenever needed the method is made, it also put
        in consideration the tax
        """

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
        """ the str overloading is set to show the whole order of the instance """
        
        name = f"Name: {self.name}\n"
        order = "Order:\n"
        for k, v in self.order.items():
            order += f"       {v} of {k}\n"
        return name + order
        


class Payers:
    """
    this class is made to be a container to 'Farers' and 'Menue'
    and puts all the needed functions in methods in the class
    """
    def __init__(self):
        """ initiate an empty list """
        self.list = []


    def add(self, obj):
        """ checks if the object passed in not none then append it to the list """
        if obj:
            self.list.append(obj)


    def money(self):
        """
        used to know the amount of cash handed by the different
        people and uses the add overloading set in wallet

        returns the Wallet.pay attribute
        """
        x = Wallet(0)
        for i in self.list:
            x += i
        return x.pay
    

    def change(self):
        """ prints the change of every object in the list """
        for i in self.list:
            # the paid amount is written for removing any conflict may be done with nameless objects
            print(f"{i.name}, paid {i.pay}, change is  {i.change}")
    

    def show(self):
        """ prints the name of all people in the list """
        print('people in list: ')
        for i in self.list:
            print(i.name)
    

    def order(self, ext: bool = False):
        """
        made for the Menu mode only
        prints the full order of all people and possibly print the
        order of each person

        :param ext: to print each's order or not
        :param type: bool, default to False
        """
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
            x = float(input(msg)) # float for tax, if smth break suspect this first
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