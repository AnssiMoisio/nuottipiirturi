from composition import Composition
from item import Item

class Column(object):
    
    def __init__(self, items, measure, start):
        self.measure = measure                          # 0,1,2,...
        self.start = start                              # e.g. 1/8 - 8/8, moment in measure
        self.notes = []                                 # notes that start in this column
        self.beams = []
        self.rests = []               
        self.find_items(items)
        self.rows = [[None]*6 for i in range(14)]       # 14 rows of the stave, 6 characters wide column
        self.add_rows()                                 # empty rows
        self.add_items()


    def find_items(self, items):
        ''' Finds items that are on this column. '''

        # items that start at this column
        for item in items:
            if item != None and item.measure == self.measure and item.start == self.start:
                self.notes.append(item)
                
        # implement: find beams over the column
        
         
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for j in range(6):
            for i in range(0,14):
                self.rows[i][j] = " "
            for i in range(2,11,2):
                self.rows[i][j] = "-"

                
    def add_items(self):
        '''
        Adds graphic items in the character list 'rows'
        according to 'notes' and other stuff ...
        '''
        
        for note in self.notes:
                
            if note.pitch > 5:
                a = 1                                   # stem points up
            else:
                a = -1                                    # stem points down
            
            if note.duration == 1:
                self.rows[note.pitch][2] = "("
                self.rows[note.pitch][3] = ")"
            
            elif note.duration == 1/2:
                self.rows[note.pitch][2] = "O"
                self.rows[note.pitch][3] = "O"
            
            elif note.duration == 1/4 or note.duration == 1/8 or note.duration == 1/16:
                self.rows[note.pitch][2] = "@"
                self.rows[note.pitch][3] = "@"


    