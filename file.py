from objects import *

def main():
    print("Hello and welcome to your favorite cli app\n\n" +
          "the app which will end all your nightmares in\n" +
          "collecting money and retuning the change back for each\n\n")
    print("Choose the mode to work on\n" +
          "enter the corresponding number of the following modes\n" +
          "1- Fare mode\n" +
          "2- Multi price fare mode\n" +
          "3- Menu Mode\n")
    mode = 0
    while mode == 0:
        mode = getter('Mode: ')
        match mode:
            case 1:
                Fare()
            case 2:
                mFare()
            case 3:
                Menu()
            case _:
                mode = 0



def Fare():
    print("Welcome to the FARE mode\n")
    price = getter("Entre the price: ", 
                          True,
                          lambda x: x > 0,
                          "Price is set!")
    mFare(price)


def mFare(price: int | None = None):
    if not price:
        print("Welcome to the Multi-Price FARE mode")
    print("\n"+
          "choose the operation to work on")
    people = Payers(Farer)
    while True:
        print("\n" +
              "Choose operation\n" +
              "1- Add payer\n" +
              "2- Show People\n" +
              "3- Show changelog\n" +
              "4- Quit\n")
        mode = getter('operation: ', True, lambda x: x in [1, 2, 3, 4])
        match mode:
            case 1:
                people.add(add_fp(price))
            case 2:
                people.show()
            case 3:
                tot_cash = people.money()
                print(f"\n{tot_cash}")
                people.change()
            case 4:
                print("\nSee you later!\nBye Bye!")
                quit()


def add_fp(price: int | None = None):
    print("\nCreating a new payer ...\n")
    name = input("Name: ")
    pay = inter(input('Paid: '))
    if not price:
        price = getter("Price: ", True, lambda x: x > 0)
    quantity = inter(input('How much: '))
    print('...')
    x = Farer(name, pay, price, quantity)
    print('\nPayer created successfully!')
    while True:
        print(f"\npayer {x.name}\n\n" +
              "further operations\n" +
              "1- Change name\n" +
              "2- Change pay\n" +
              "3- Change amount\n" +
              "4- Show HIS change\n" +
              "5- Show all data\n"
              "6- Delete payer\n" +
              "7- Save\n")
        mode = getter("operation: ", True,
                      lambda x: x in [1, 2, 3, 4, 5, 6, 7])
        match mode:
            case 1:
                x.name = input("New name: ")
            case 2:
                x.change_pay(inter(input('New pay: ')))
            case 3:
                x.change_amount(inter(input('How much: ')))
            case 4:
                print(f"\n{x.change}")
            case 5:
                print(f"\n{x}")
            case 6:
                del x
                return None
            case 7:
                return x


def Menu():
    print("Welcome to the Menu mode")


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


if __name__ == "__main__":
    main()
