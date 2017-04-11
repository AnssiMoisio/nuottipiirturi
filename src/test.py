from item import Item
from column import Column
from composition import Composition
from char_graphics import CharGraphics

def main():
    item = Item(Item.NOTE, Item.C, 0, 0, 1/4)       #(item_type, pitch, measure, start, duration)
    item2 = Item(Item.NOTE, Item.D, 0, 1/4, 1/4)
    item3 = Item(Item.NOTE, Item.E, 0, 2/4, 1/4)
    item4 = Item(Item.NOTE, Item.F, 0, 3/4, 1/4)
    item5 = Item(Item.NOTE, Item.c1, 0, 4/4, 1/4)
    item6 = Item(Item.NOTE, Item.d1, 0, 5/4, 1/4)
    item7 = Item(Item.NOTE, Item.e1, 0, 6/4, 1/4)
    item8 = Item(Item.NOTE, Item.f1, 0, 7/4, 1/4)
    
    composition = Composition(None, None, 0, 1)     #(name, creator, meter, length)
    Composition.add_item(composition,item)
    Composition.add_item(composition,item2)
    Composition.add_item(composition,item3)
    Composition.add_item(composition,item4)
    Composition.add_item(composition,item5)
    Composition.add_item(composition,item6)
    Composition.add_item(composition,item7)
    Composition.add_item(composition,item8)
  
    #column = Column(composition, 0, 0)                # (composition, measure, start)
    #column = Column(composition, 0, 1)
    
    CharGraphics(composition)

main()