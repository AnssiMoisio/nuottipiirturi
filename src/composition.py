from item import Item 

class Composition(object):
    
    def __init__(self, array, name, creator, meter, length):
        self.array = array                      # list of all notes, rests and syllables (=items) in arbitrary order
        self.creator = creator                  # string
        self.name = name                        # string
        self.meter = meter                      # beats per measure, only 3/4 or 4/4 for now
        self.length = length                    # length of the melody in measures, integer
        
    def add_item(self, item_type, pitch, measure, start, duration):
        item = Item(item_type, pitch, measure, start, duration)
        self.array.append(item)
        
    def remove_item(self, item):
        self.array.remove(item)
