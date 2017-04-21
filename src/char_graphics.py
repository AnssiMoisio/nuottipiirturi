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
             
        for i in range(len(columns)):                                                               # for each column in measure
            col = Column(composition.array, composition.beams, measure, (shortest*i) + shortest)    # create new column
            columns[i] = col                                                                        # add to the list of columns of this measure
        
        measure_matrix = [[None]*15 for i in range(len(columns))]
        i = 0
        j = 0
        for j in range(15):
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
        whole = [" "] * 15
        for k in range(len(self.measures)):                                            # for each measure
            for j in range(15):                                                        # for each row
                self.clef()
                whole_row = self.measures[k][0][j][0]                                  # add first char of first column of this row
                for i in range(len(self.measures[k])):                                 # for each column in matrix
                    for c in range(6):                                                 # for each char
                        if i !=0 or c != 0:
                            whole_row = whole_row + self.measures[k][i][j][c]              # add next char
                
                if j in {2,4,6,8,10}: whole_row = whole_row + "---|"
                elif j in {3,5,7,9}: whole_row = whole_row + "   |"
                else: whole_row = whole_row + "    "
                whole[j] = whole[j] + whole_row
        for j in range(15):
            print(whole[j])
                
                
    def clef(self):
        self.measures[0][0][0][0]  = "              "
        self.measures[0][0][1][0]  = "     /'\      "
        self.measures[0][0][2][0]  = "----|--/------"
        self.measures[0][0][3][0]  = "    | /       "
        self.measures[0][0][4][0]  = "----\/--------"
        self.measures[0][0][5][0]  = "    /\        "
        self.measures[0][0][6][0]  = "---/-|--------"
        self.measures[0][0][7][0]  = "  / _|_       "
        self.measures[0][0][8][0]  = "-|-\-|-\------"
        self.measures[0][0][9][0]  = " \___|_/      "
        self.measures[0][0][10][0] = "------\-------"
        self.measures[0][0][11][0] = "  @@   \      "
        self.measures[0][0][12][0] = "   \___/      "
        self.measures[0][0][13][0] = "              "
    
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

        