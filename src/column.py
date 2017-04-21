class Column(object):
    
    def __init__(self, items, beams, measure, start):
        self.measure = measure                          # 0,1,2,...
        self.start = start                              # e.g. 1/8 - 8/8, moment in measure
        self.notes = []                                 # notes that start in this column
        self.beams = beams
        self.rests = []               
        self.find_items(items)
        self.rows = [[None]*6 for i in range(15)]       # 14 rows of the stave, 6 characters wide column
        self.add_rows()                                 # empty rows
        self.add_stems()
        self.add_notes()
        self.create_beams()
        

    def find_items(self, items):
        ''' Finds items that are on this column. '''

        # notes
        for item in items:
            if item.measure == self.measure and item.start == self.start:
                self.notes.append(item)
                
        # implement: all kinds of shit
        
         
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for j in range(6):
            for i in range(0,15):
                self.rows[i][j] = " "
            for i in range(2,11,2):
                self.rows[i][j] = "-"

                
    def add_notes(self):
        '''
        Adds graphic items in the character list 'rows'
        according to the list 'notes'
        '''
        
        for note in self.notes:


            if note.duration == 1:
                self.rows[note.pitch][2] = "("
                self.rows[note.pitch][3] = ")"
            
            elif note.duration == 1/2:
                self.rows[note.pitch][2] = "O"
                self.rows[note.pitch][3] = "O"
            
            elif note.duration == 1/4 or note.duration == 1/8 or note.duration == 1/16:
                self.rows[note.pitch][2] = "@"
                self.rows[note.pitch][3] = "@"
            
            
    def add_stems(self):
        beamed = []
        flagged = []
        for note in self.notes:
            for beam in self.beams:
                if note in beam.notes:
                    beamed.append(note)
                    
        for note in self.notes:
            if note not in beamed:
                flagged.append(note)
                
        count = len(flagged)
        if count == 1:
            if flagged[0].duration < 1:
                self.create_stem(flagged[0], flagged[0])
                self.create_flag(flagged[0], flagged[0])
        
        elif count > 1:

            for i in range(count - 1):                                       #sort notes from lowest to highest
                for i in range(count - 1):
                    if flagged[i].pitch > flagged[i+1].pitch:
                        temp = flagged[i]
                        flagged[i] = flagged[i+1]
                        flagged[i+1] = temp
                        
            for i in range(flagged[0].pitch, flagged[count-1].pitch):
                self.rows[i][3] = "|"
            
            if flagged[0].pitch > 5:
                self.create_stem(flagged[0],flagged[0])
                self.create_flag(flagged[0],flagged[0])
                    
        for note in beamed:
            for beam in self.beams:
                if note in beam.notes:
                    for k in range(beam.pitch, note.pitch):
                        self.rows[k][3] = "|"
    
     
                       
    def create_stem(self, note, ref):
        if ref.pitch > 5: a = 1                         # stem points up
        else: a = -1                                    # stem points down
        

        if note.duration < 1:
            for k in range(1,5):
                self.rows[note.pitch - k*a][3] = "|"
                
                
    def create_flag(self, note, ref):
        if ref.pitch > 5: a = 1                         # stem points up
        else: a = -1                                    # stem points down
                
        if note.duration == 1/8:
            if a == 1:
                self.rows[note.pitch - 2*a][4] = "/"
                self.rows[note.pitch - 3*a][4] = "\\"
                self.rows[note.pitch - 4*a][3] = "\\"
            else:
                self.rows[note.pitch - 2*a][4] = "\\"
                self.rows[note.pitch - 3*a][4] = "/"
                self.rows[note.pitch - 4*a][3] = "/"
                
        elif note.duration == 1/16:
            if a == 1:
                self.rows[note.pitch - 1*a][4] = "/"
                self.rows[note.pitch - 2*a][4] = "\\"
                self.rows[note.pitch - 3*a][4] = "\\"
                self.rows[note.pitch - 4*a][3] = "\\"
            else:
                self.rows[note.pitch - 1*a][4] = "\\"
                self.rows[note.pitch - 2*a][4] = "/"
                self.rows[note.pitch - 3*a][4] = "/"
                self.rows[note.pitch - 4*a][3] = "/"
        
        
    def create_beams(self):
        for beam in self.beams:
            if beam.measure == self.measure:
                if beam.start < self.start and beam.end > self.start:
                    for i in range(6):
                        self.rows[beam.pitch][i] = "="
                        
                elif beam.start == self.start:
                    for i in range(3,6):
                        self.rows[beam.pitch][i] = "="
                        
                elif beam.end == self.start:
                    for i in range(4):
                        self.rows[beam.pitch][i] = "="
                        
                    