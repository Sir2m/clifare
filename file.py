from objects import *

def main():
    print("Hello and welcome to your favorite cli app\n\n" +
          "the app which will end all your nightmares in\n" +
          "collecting money and retuning the change back for each\n\n")
    print("Choose the mode to work on\n" +
          "enter the corresponding number of the following modes\n" +
          "1- Fare mode\n" +
          "2- multi price fare mode\n" +
          "3- Menu Mode\n")
    mode = 0
    while mode == 0:
        mode = get_int_input('Mode: ')
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
    price = get_int_input("Entre the price: ", 
                          True,
                          lambda x: x > 0,
                          "Price is set!")
    mFare(price)


def mFare(price: int | None = None):
    if not price:
        print("Welcome to the Multi-Price FARE mode")
    print("\n"+
          "choose the operation to work on")
    


def get_int_input(msg:str, set_stat:bool = False, bool_cond = None, set_msg: str | None = None):
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


def Menu():
    print("Welcome to the Menu mode")


if __name__ == "__main__":
    main()
