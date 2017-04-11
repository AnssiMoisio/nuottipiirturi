from item import Item
from composition import Composition
from column import Column

class CharGraphics(object):
    
    def __init__(self, composition):
        self.measures = []                          # list of measures
        #self.sheet = []
        self.create_measure(composition, 0)
        #self.create_sheet()
        
    def create_measure(self, composition, measure):
        
        shortest = 1
        for item in composition.array:               # e.g. if shortest note is 1/8, measure contains 16 columns
            if measure == item.measure:              #
                if item.duration < shortest:         #
                    shortest = item.duration         #
                    
        columns = int(2/shortest) * [None]              # list of columns in this measure
        
        for i in range(int(2/shortest)):                                    # for each column in measure
            items = []                                                      # new list for items that are in this column
            for item in composition.array:                                  # for each item in composition 
                if item.measure == measure and item.start == i*shortest:    # if item is in this column
                    items.append(item)                                      # add to list
            
            col = Column(items, measure, shortest*i)                        # create new column
            columns[i] = col                                                # add to the list of columns of this measure
        
        
        measurerows = columns[0].rows                                       # this will be the printable measure, list of 11 rows
        for k in range(11):                                                 # for each row
            for n in range (1,len(columns)):                                          # for each column
                measurerows[k] = measurerows[k] + columns[n].rows[k]            # add the row k of column to row k of measurerows
           
        for row in measurerows:        
            print(row)
            
    def create_sheet(self):
        '''
        Creates a matrix from columns array,
        containing all columns, the whole sheet music (and prints it?)
        '''
        
        #for k in range(11):
            #for i in range(len(self.columns)):
            #print(self.columns[0].rows[k] + self.columns[1].rows[k])
                    
    
    #def print_sheet(self):