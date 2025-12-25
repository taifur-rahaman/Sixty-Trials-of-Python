
from merger import *
from utils import *


beautify("List Merger")

while True:
    list_1 = input("Enter list 1: ").split()
    list_2 = input("Enter list 2: ").split()
    
    merger = ListMerger(list_1, list_2)
    print(merger.marge_lists())

    if input("Do you want to continue? (y/n): ") == "n":
        exit()