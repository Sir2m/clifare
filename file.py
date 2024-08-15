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
    people = Payers()
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
                quiter()


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
        print(f"\nPayer {x.name}\n\n" +
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
    print("\n"+
          "choose the operation to work on")
    people = Payers()
    while True:
        print("\n" +
              "Choose operation\n" +
              "1- Add customer\n" +
              "2- Show People\n" +
              "3- Add to Menu\n" +
              "4- Show Menu\n" +
              "5- Change Menu price\n" +
              "6- Add tax\n" +
              "7- Show full order\n" +
              "8- Show extended order\n"
              "9- Quit\n")
        mode = getter("operation: ", True,
                      lambda x: x in [_ for _ in range(1, 10)])
        match mode:
            case 1:
                people.add(add_mp())
            case 2:
                people.show()
            case 3:
                print("Adding item\n")
                Menue.add_item(input("Item: "))
                print("\nItem added successfully")
            case 4:
                Menue.print_menu()
            case 5:
                Menue.edit_price()
            case 6:
                Menue.add_tax()
            case 7:
                people.order(False)
            case 8:
                people.order(True)
            case 9:
                quiter()


def add_mp():
    print("\nCreating a new customer ...\n")
    name = input("Name: ")
    print('...')
    x = Menue(name)
    print('\nCustomer created successfully!')
    while True:
        print(f"\nCustomer {x.name}\n\n" +
              "further operations\n" +
              "1- Add order\n" +
              "2- Change name\n" +
              "3- Calc order cost\n" +
              "4- Pay!\n" +
              "5- Show HIS change\n" +
              "6- Show Order\n"
              "7- Delete payer\n" +
              "8- Save\n")
        mode = getter("operation: ", True,
                      lambda x: x in [_ for _ in range(1, 9)])
        match mode:
            case 1:
                inpi = input("Order item: ")
                inpii = inter(input("How much: "))
                x.add_order(inpi, inpii)
                print("\nOrder saved\n")
            case 2:
                x.name = input("New name: ")
            case 3:
                x.get_cost()
                print(f"\nOrder cost: {x.cost}\n")
            case 4:
                x.to_pay()
            case 5:
                if x.change:
                    print(f"\nChange: {x.change}\n")
                else:
                    print("Didn't pay yet")
            case 6:
                print(f"\n{x}")
            case 7:
                del x
                return None
            case 8:
                try:
                    if x.pay and (x.change > 0):
                        return x
                    else:
                        print("\nYou seems didn't stat the pay, PAY FIRST!\n")
                except KeyboardInterrupt:
                    quit()
                except:
                    pass


def quiter():
    print("\nSee you later!\nBye Bye!")
    quit()

if __name__ == "__main__":
    main()
