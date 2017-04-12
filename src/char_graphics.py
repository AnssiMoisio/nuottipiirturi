from item import Item
from composition import Composition
from column import Column

class CharGraphics(object):
    
    def __init__(self, composition):
        self.measures = []
        self.measures.append(self.create_measure(composition, 0))
        #self.sheet = []
        self.print_sheet()
        
    def create_measure(self, composition, measure):
        '''
        Creates one printable measure.
        '''
        
        shortest = 1
        for item in composition.array:               # e.g. if shortest note is 1/8, measure contains 16 columns
            if measure == item.measure:              #
                if item.duration < shortest:         #
                    shortest = item.duration         #
                    
        columns = int(2/shortest) * [None]           # list of columns in this measure
        

        
        for i in range(int(2/shortest)):                                                          # for each column in measure
            items = []                                                                            # new list for items that are in this column
            for item in composition.array:                                                        # for each item in composition 
                if item.measure == measure and item.start == ((shortest*i) + (2*shortest))/2:     # if item is in this column
                    items.append(item)                                                            # add to list
                    
            col = Column(items, measure, ((shortest*i) + (2*shortest))/2)                         # create new column
            columns[i] = col                                                                      # add to the list of columns of this measure
        
        measurerows = columns[0].rows                                       # this will be the printable measure, list of 14 rows
        for k in range(14):                                                 # for each row in stave
            for n in range (1,len(columns)):                                # for each column of the measure
                measurerows[k] = measurerows[k] + columns[n].rows[k]        # add the row k of this column to row k of the measure stave
           
        return measurerows
            
            
    def create_sheet(self):
        '''
        Collects the measures to create a sheet music.
        '''


    def print_sheet(self):
        for i in range(len(self.measures)):
            for row in self.measures[i]:        
                print(row)
    
    
    #def clef(self):
    
        #       /'\
        #  --- |--/
        #      | / 
        #  -----V--
        #      /\  
        #  ---/-|--
        #    / _|_ 
        #  -|-\-|-\
        #   \___|_/
        #  -----|--
        #   @@   \ 
        #    \___/ 

        