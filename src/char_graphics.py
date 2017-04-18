from item import Item
from composition import Composition
from column import Column

class CharGraphics(object):
    
    
    
    
    def __init__(self, composition):
        
        self.measures = []
        self.add_measures(composition)
        #self.add_tie(Item.c1, 0, 7, 9)
        self.print_sheet()
        
        
    def create_measure(self, composition, measure):
        '''
        Creates one printable measure and returns it as X * 14 matrix, where X is the number of columns,
        which is determined by the shortest note length. e.g. if shortest note is 1/8, measure contains 8 columns.
        '''
        
        shortest = 1
        for item in composition.array:               # e.g. if shortest note is 1/8, measure contains 8 columns
            if measure == item.measure:              #
                if item.duration < shortest:         #
                    shortest = item.duration         #
                    
        columns = int(1/shortest) * [None]           # list of columns in this measure
             
        for i in range(len(columns)):                                                             # for each column in measure
            col = Column(composition.array, measure, (shortest*i) + shortest)                     # create new column
            columns[i] = col                                                                      # add to the list of columns of this measure
        
        measure_matrix = [[None]*14 for i in range(len(columns))]
        i = 0
        j = 0
        for j in range(14):
            for i in range(len(columns)):
                measure_matrix[i][j] = columns[i].rows[j]

        return measure_matrix
    
    
    def add_measures(self, composition):
        for i in range(composition.length):
            measure = self.create_measure(composition, i)
            self.measures.append(measure)
            

    
    
    def add_tie(self, pitch, measure, start, stop):
        for i in range(start,stop):
            self.measures[measure][i][pitch] = self.tie1


    def print_sheet(self):

        for k in range(len(self.measures)):                                            # for each measure
            for j in range(14):                                                        # for each row
                whole_row = self.measures[k][0][j]                                     # add first column of this row
                for i in range(len(self.measures[k]) - 1):                             # for each column in matrix
                    whole_row = whole_row + self.measures[k][i+1][j]                   # add next string
    
                print(whole_row)
                
                
    #def clef(self):
    
        #       /'\
        #  --- |--/
        #      | / 
        #  ----\/--
        #      /\  
        #  ---/-|--
        #    / _|_ 
        #  -|-\-|-\
        #   \___|_/
        #  ------\--
        #    @@   \ 
        #     \___/ 

        