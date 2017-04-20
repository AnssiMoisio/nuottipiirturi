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
        
        self.add_stems()
        self.add_notes()

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
            for i in range(0,14):
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
        count = len(self.notes)
        
        if count == 1:
            note = self.notes[0]
            if note.duration < 1:
                if note.pitch > 5: a = 1        # stem points up
                else: a = -1                    # stem points down
                for k in range(1,5):
                    self.rows[note.pitch - k*a][3] = "|"
        
        elif count > 1:
            highest = 0
            lowest = 14
            for i in range(count - 1):                                       #sort notes from lowest to highest
                for i in range(count - 1):
                    if self.notes[i].pitch > self.notes[i+1].pitch:
                        temp = self.notes[i]
                        self.notes[i] = self.notes[i+1]
                        self.notes[i+1] = temp
                    
            for i in range(1, count):
                if self.notes[i-1].pitch > 5: a = 1             # stem points up
                else: a = -1                                    # stem points down
                
                dif = self.notes[i].pitch - self.notes[i-1].pitch
                if  dif < 5:
                    if a == 1:
                        for k in range(1,5):
                            self.rows[self.notes[i].pitch - k*a][3] = "|"
                    else:
                        for k in range(1,5):
                            self.rows[self.notes[i-1].pitch - k*a][3] = "|"
                    i +=1
                    
                elif i+1 > count-1 or self.notes[i+1] - self.notes[i] > 4:
                    if self.notes[i].pitch > 5: a = 1                           # stem points up
                    else: a = -1                                                # stem points down
                    for k in range(1,5):
                        self.rows[self.notes[i].pitch - k*a][3] = "|"                
   
                        
    def create_stem(self, note):
        if note.pitch > 5: a = 1        # stem points up
        else: a = -1                    # stem points down
        if note.duration > 1/8:
            for k in range(1,5):
                self.rows[note.pitch - k*a][3] = "|"
        elif note.duration == 1/8:
            for k in range(1,5):
                self.rows[note.pitch - k*a][3] = "|"
            self.rows[note.pitch - 2*a][4] = "\\"
            self.rows[note.pitch - 3*a][4] = "\\"
            self.rows[note.pitch - 4*a][3] = "\\"
                  