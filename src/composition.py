from item import Item

class Composition(object):
    
    def __init__(self, name, creator, meter, length):
        '''
        @param items: all notes and rests in arbitrary order
        @param meter: beats per measure
        @param length: length of the melody in measures, integer
        '''
        self.items = []                         # 
        self.beams = []
        self.creator = creator                  # string
        self.name = name                        # string
        self.meter = meter                      # only 3/4 or 4/4 for now
        self.length = length                    # 
        
        
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def add_beam(self,beam):
        self.beams.append(beam)
        
    def fill_holes(self):
        ''' Fills empty beats with rests. This should be done last.'''
        
        for measure in range(self.length):
            shortest = 1
            for item in self.items:                         # e.g. if shortest note is 1/8, measure contains 8 columns
                if measure == item.measure:                 #
                    if item.duration < shortest:            #
                        shortest = item.duration            #
                        
            for i in range(1, int(1/shortest) + 1):
                a = 0
                for item in self.items:
                    if item.item_type == Item.NOTE and measure == item.measure:
                        if item.start == i*shortest:
                            a += 1
                        elif item.start < (i*shortest) and (item.start + item.duration) > (i*shortest):
                            a += 1
                if a == 0:
                    rest = Item(Item.REST, None, measure, i*shortest, shortest)       # (item_type, pitch, measure, start, duration)
                    self.add_item(rest)
                        