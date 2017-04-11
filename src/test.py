from item import Item
from column import Column
from composition import Composition

def main():
    item = Item(Item.NOTE, Item.A, 0, 0, 1/4)
    array = [item]
    composition = Composition(array, None, None, 0, 1)
    column = Column(composition,0,0)
    

main()