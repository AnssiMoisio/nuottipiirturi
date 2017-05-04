from column import Column

class CharGraphics(object):
    
    def __init__(self, composition):
        
        self.measures = []
        self.add_measures(composition)
        self.print_sheet(composition)
        
    
    def add_measures(self, composition):
        
        for i in range(composition.length):
            measure = self.create_measure(composition, i)
            self.measures.append(measure)
            
            
    def create_measure(self, composition, measure):
        '''
        Creates one printable measure and returns it as X * 16 matrix, where X is the number of columns,
        which is determined by the shortest note duration. e.g. if shortest note is 1/8, measure consists of 8 columns.
        '''
        
        shortest = 1
        for note in composition.notes:               # e.g. if shortest note/rest is 1/8, measure contains 8 columns
            if measure == note.measure:              #
                if note.duration < shortest:         #
                    shortest = note.duration         #
        for rest in composition.rests:
            if measure == rest.measure:              #
                if rest.duration < shortest:         #
                    shortest = rest.duration         #
                    
        columns = int(1/shortest) * [None]           # list of columns in this measure
             
        for i in range(len(columns)):                                           # for each column in measure
            col = Column(composition, measure, (shortest*i) + shortest)         # create new column
            columns[i] = col                                                    # add to the list of columns of this measure
        
        measure_matrix = [[None]*16 for i in range(len(columns))]           # create meatrix for the whole measure
        for j in range(16):                                                 # 
            for i in range(len(columns)):                                   #
                measure_matrix[i][j] = columns[i].rows[j]                   # fill matrix according to list of columns

        return measure_matrix
            
            
    def add_tie(self, pitch, measure, start, stop):
        
        for i in range(start,stop):
            self.measures[measure][i][pitch] = self.tie1
            
            
    def print_sheet(self, composition):
        print(composition.creator,": ",composition.name)
        whole = [" "] * 16
        for k in range(len(self.measures)):                                            # for each measure
            if k in {0,3,6,9,12,15,18}: self.clef(k,composition)
            for j in range(16):                                                        # for each row
                whole_row = ""                                                          
                for i in range(len(self.measures[k])):                                 # for each column in matrix
                    for c in range(6):                                                 # for each char
                        whole_row = whole_row + self.measures[k][i][j][c]              # add next char
                
                if j in {2,4,6,8,10}: whole_row = whole_row + "---|"                   # add measure bar
                elif j in {3,5,7,9}: whole_row = whole_row + "   |"
                else: whole_row = whole_row + "    "
                whole[j] = whole[j] + whole_row
            
            if k in {2,5,8,11,14,17}:                                                       # line break after 3 measures
                for j in range(16):
                    print(whole[j])
                whole = [" "] * 16
                print("\n\n\n")
        if k not in {2,5,8,11,14,17}:
            for j in range(16):
                print(whole[j])
            print("\n\n\n")

                
    def clef(self,k,composition):
        
        list = [None]*16
        
        list[0]  = "            "
        list[1]  = "     /'\    "
        list[2]  = "----|--/----"
        list[3]  = "    | /     "
        list[4]  = "----\/------"
        list[5]  = "    /\      " 
        list[6]  = "---/-|------"
        list[7]  = "  / _|_     "
        list[8]  = "-|-\-|-\----"
        list[9]  = " \___|_/    "
        list[10] = "------\-----" 
        list[11] = "  @@   \    "
        list[12] = "   \___/    "
        list[13] = "            "
        list[14] = "            "
        list[15] = "            "
        for j in range(16):
            if j in composition.flats:
                list[j]  = list[j] + "b"
            elif j in composition.sharps:
                list[j] = list[j] + "#"
            elif j in {2,4,6,8,10}:
                list[j] = list[j] + "-"
            else:
                list[j] = list[j] + " "
                
        for j in range(16):
            self.measures[k][0][j][0] = list[j] + self.measures[k][0][j][0]
            
