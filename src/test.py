from item import Item
from column import Column
from composition import Composition
from char_graphics import CharGraphics

def main():
    item = Item(Item.NOTE, Item.A, 0, 0, 1/4)       #(item_type, pitch, measure, start, duration)
    item2 = Item(Item.NOTE, Item.C, 0, 1, 1/4)
    
    composition = Composition(None, None, 0, 1)     #(name, creator, meter, length)
    Composition.add_item(composition,item)
    Composition.add_item(composition,item2)
    
    #column = Column(composition, 0, 0)                # (composition, measure, start)
    #column = Column(composition, 0, 1)
    
    CharGraphics(composition)

main()