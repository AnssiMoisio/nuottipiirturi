from item import Item 

class Composition(object):
    
    def __init__(self, name, creator, meter, length):
        '''
        @param array: all notes, rests and syllables (=items) in arbitrary order
        @param meter: beats per measure
        @param length: length of the melody in measures, integer
        '''
        self.array = []                         # 
        self.creator = creator                  # string
        self.name = name                        # string
        self.meter = meter                      # only 3/4 or 4/4 for now
        self.length = length                    # 
        
        
    def add_item(self, item):
        self.array.append(item)
        
        
    def remove_item(self, item):
        self.array.remove(item)
