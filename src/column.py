from composition import Composition
from item import Item

class Column(object):

    wholenote = "  ()"
    halfnote = " 00"
    quarternote_odd = " @@"
    quarternote_even = "-@@"
    eigthnote_odd = " oo"
    eigthnote_even = "-oo"
    stem_odd = "  |"
    stem_even = "--|"
    bar = "==="
    
    def __init__(self, items, measure, start):
        self.measure = measure                          # 0,1,2,...
        self.start = start                              # e.g. 1/8 - 8/8, moment in measure
        self.starting = []                              # the items that start in this column                   
        self.starting_items(items)
        self.rows = 11 * [None]                         # 11 strings of 3 characters, the 11 rows of the stave
        self.add_rows()                                 # empty rows
        self.add_items()

        
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for i in range(0,10,2):
            self.rows[i] = "---"
        for i in range(1,11,2):
            self.rows[i] = "   "
        self.rows[10] = "   "
        

    def starting_items(self, items):
        ''' Finds items that are on this column. '''

        # items that start at this column
        for item in items:
            if item != None and item.measure == self.measure and item.start == self.start:
                self.starting.append(item)
                
        # implement: find bars over the column

                
    def add_items(self):
        '''
        Adds graphic items in the character list 'rows'
        according to 'starting' items and other stuff ...
        '''
        
        # starting list
        for i in range(len(self.starting)):
            if self.starting[i] != None and self.starting[i].item_type == Item.NOTE:
                
                if self.starting[i].pitch > 1: a = 1        # stem points up
                else: a = -1                                # stem points down
                
                if self.starting[i].pitch % 2 == 0:          # note is on even row
                    quarternote = self.quarternote_even
                    stem1 = self.stem_odd
                    stem2 = self.stem_even
                    #halfnote = self.halfnote_even            add all other types
                    
                else:                                         # note is on odd row
                    quarternote = self.quarternote_odd
                    stem1 = self.stem_even
                    stem2 = self.stem_odd
                
                if self.starting[i].duration == 1/4:
                    self.rows[self.starting[i].pitch]           = quarternote
                    self.rows[self.starting[i].pitch - (1*a)]   = stem1
                    self.rows[self.starting[i].pitch - (2*a)]   = stem2
               
                
        #### test print
        #for i in range(len(self.rows)):
        #    print(self.rows[i])
        ####
    