from utils import *
from swapper import *

beautify("Tuple Swapper")

while True:
    tuple_ = tuple(input("Enter tuple elements separated by space: ").split())
    Swapper.show_index(tuple_)
    swap_tuple_ = tuple_
    while True:
        try:
            index_1 = int(input("Which element to Swap: "))
            index_2 = int(input("With which element to Swap: "))
            swap_tuple_ = Swapper.swap(tuple_, index_1, index_2)
            beautify("Swapped Tuple")
            Swapper.show_index(swap_tuple_)
        except IndexError:
            print("Invalid index")
        except ValueError:
            print("Invalid input")
        else:
            tuple_ = swap_tuple_
            if input("Do you want to swap again? (y/n): ") == "n":
                break
    if input("Do you want to try again? (y/n): ") == "n":
        break

