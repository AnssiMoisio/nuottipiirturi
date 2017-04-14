from composition import Composition
from item import Item

class Column(object):

    wholenote_odd           = " () "
    wholenote_even          = "-()-"
    halfnote_odd            = " OO "
    halfnote_even           = "-OO-"
    head_odd                = " @@ "
    head_even               = "-@@-"
    stem_odd                = "  | "
    stem_even               = "--|-"
    eighth_stem1_even       = "  |\\"
    eighth_stem1_odd        = "--|\\"
    eighth_stem2_even       = "  \ "
    eighth_stem2_odd        = "--\-"

    beam                    = "===="
    
    def __init__(self, items, measure, start):
        self.measure = measure                          # 0,1,2,...
        self.start = start                              # e.g. 1/8 - 8/8, moment in measure
        self.starting = []                              # the items that start in this column                   
        self.starting_items(items)
        self.rows = 14 * [None]                         # 11 strings of 3 characters, the 11 rows of the stave
        self.add_rows()                                 # empty rows
        self.add_items()

        
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for i in range(0,14):
            self.rows[i] = "    "
        for i in range(2,11,2):
            self.rows[i] = "----"
        

    def starting_items(self, items):
        ''' Finds items that are on this column. '''

        # items that start at this column
        for item in items:
            if item != None and item.measure == self.measure and item.start == self.start:
                self.starting.append(item)
                
        # implement: find beams over the column

                
    def add_items(self):
        '''
        Adds graphic items in the character list 'rows'
        according to 'starting' items and other stuff ...
        '''
        
        # starting list
        for i in range(len(self.starting)):
            if self.starting[i] != None and self.starting[i].item_type == Item.NOTE:
                
                if self.starting[i].pitch > 5:
                    a = 1                                   # stem points up
                else:
                    a = -1                                    # stem points down
                    self.eighth_stem2_even = "  / "
                    self.eighth_stem2_odd = "--/-"
                    self.eighth_stem1_even = "  |/"
                    self.eighth_stem1_odd = "--|/"
                    
                if self.starting[i].pitch % 2 == 0:          # note is on even row
                    head = self.head_even
                    stem1 = self.stem_odd
                    stem2 = self.stem_even
                    e_stem1 = self.eighth_stem1_odd
                    e_stem2 = self.eighth_stem1_even
                    e_stem = self.eighth_stem2_odd
                    #halfnote = self.halfnote_even            add all other types
                    
                else:                                         # note is on odd row
                    head = self.head_odd
                    stem1 = self.stem_even
                    stem2 = self.stem_odd
                    e_stem1 = self.eighth_stem1_even
                    e_stem2 = self.eighth_stem1_odd
                    e_stem = self.eighth_stem2_even
     
                if self.starting[i].duration == 1/4:
                    self.rows[self.starting[i].pitch]           = head
                    self.rows[self.starting[i].pitch - (1*a)]   = stem1
                    self.rows[self.starting[i].pitch - (2*a)]   = stem2
                    self.rows[self.starting[i].pitch - (3*a)]   = stem1
                    self.rows[self.starting[i].pitch - (4*a)]   = stem2
               
                elif self.starting[i].duration == 1/8:
                    self.rows[self.starting[i].pitch]           = head
                    self.rows[self.starting[i].pitch - (1*a)]   = stem1
                    self.rows[self.starting[i].pitch - (2*a)]   = e_stem1
                    self.rows[self.starting[i].pitch - (3*a)]   = e_stem2
                    self.rows[self.starting[i].pitch - (4*a)]   = e_stem
