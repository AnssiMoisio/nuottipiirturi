from item import Item
from beam import Beam
from composition import Composition
from char_graphics import CharGraphics

def main():
    
    item = Item(Item.NOTE, Item.F, 0, 1/8, 1/8)       # (item_type, pitch, measure, start, duration)
    item2 = Item(Item.NOTE, Item.A, 0, 2/8, 1/8)
    item3 = Item(Item.NOTE, Item.A, 0, 5/8, 1/4)
    item4 = Item(Item.NOTE, Item.b1, 0, 4/8, 1/8)
    item5 = Item(Item.NOTE, Item.C, 0, 3/8, 1/8)
    item6 = Item(Item.NOTE, Item.A, 0, 3/8, 1/8)
    item7 = Item(Item.NOTE, Item.B, 0, 7/8, 1/8)
    item8 = Item(Item.NOTE, Item.f1, 0, 8/8, 1/8)
    
    composition = Composition(None, None, 0, 2)       # (name, creator, meter, length)
    
    notes = [item, item2]
    beam = Beam(notes)
    Composition.add_beam(composition,beam)
    
    notes2 = [item7, item8]
    beam = Beam(notes2)
    Composition.add_beam(composition,beam)

    
    Composition.add_item(composition,item)
    Composition.add_item(composition,item2)
    Composition.add_item(composition,item3)
    Composition.add_item(composition,item4)
    Composition.add_item(composition,item5)
    Composition.add_item(composition,item6)
    Composition.add_item(composition,item7)
    Composition.add_item(composition,item8)
    
    
    item12 = Item(Item.NOTE, Item.F, 1, 1/16, 1/16)       # (item_type, pitch, measure, start, duration)
    item2 = Item(Item.NOTE, Item.C, 1, 2/16, 1/16)
    item3 = Item(Item.NOTE, Item.D, 1, 3/16, 1/16)
    item4 = Item(Item.NOTE, Item.F, 1, 2/8, 1/2)
    item5 = Item(Item.NOTE, Item.G, 1, 11/16, 1/8)
    item6 = Item(Item.NOTE, Item.A, 1, 6/8, 1/16)
    item7 = Item(Item.NOTE, Item.b1, 1, 7/8, 1/8)
    item8 = Item(Item.NOTE, Item.E, 1, 1, 1/16)
    
    notes3 = [item7, item5]
    beam = Beam(notes3)
    Composition.add_beam(composition,beam)

    Composition.add_item(composition,item12)
    Composition.add_item(composition,item2)
    Composition.add_item(composition,item3)
    Composition.add_item(composition,item4)
    Composition.add_item(composition,item5)
    Composition.add_item(composition,item6)
    Composition.add_item(composition,item7)
    Composition.add_item(composition,item8)
    
    CharGraphics(composition)

main()