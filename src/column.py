from composition import Composition

class Column(object):
    
    def __init__(self, composition, measure, start):
        self.measure = measure                          # 0,1,2,...
        self.start = start                              # e.g. 1/8 - 8/8, moment in measure
        self.notes = []                                 # notes that start in this column
        self.beams = []
        self.rests = []               
        self.find_items(composition)
        self.rows = [[None]*6 for i in range(16)]       # 14 rows of the stave, 6 characters wide column
        self.add_rows()                                 # empty rows
        self.add_stems()
        self.create_heads()
        self.create_rests()
        self.create_beams()
        

    def find_items(self, comp):
        ''' Finds items that are on this column. '''

        for note in comp.notes:
            if note.measure == self.measure and note.start == self.start:
                self.notes.append(note)
                
        for rest in comp.rests:
            if rest.measure == self.measure and rest.start == self.start:
                self.rests.append(rest)
                    
        for note in self.notes:
            for rest in self.rests:
                if note.start == rest.start:
                    Composition.remove_rest(comp, rest.measure, rest.start)
                    print("Nuotti ja tauko paallekain. Tauko poistettu.")
                
        for beam in comp.beams:
            if beam.measure == self.measure:
                self.beams.append(beam)
        
         
    def add_rows(self):
        ''' Adds empty rows for this column. '''
        
        for j in range(6):
            for i in range(0,16):
                self.rows[i][j] = " "
            for i in range(2,11,2):
                self.rows[i][j] = "-"

                
    def create_heads(self):
        '''
        Adds note heads in the character list 'rows'
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
            if flagged[0].pitch > 5: a = 1
            else: a = -1
            self.create_flag(flagged[0].pitch, flagged[0].pitch - a*4, flagged[0].duration)
        
        elif count > 1:
            for i in range(count - 1):                                       #sort notes from lowest to highest
                for i in range(count - 1):
                    if flagged[i].pitch > flagged[i+1].pitch:
                        temp = flagged[i]
                        flagged[i] = flagged[i+1]
                        flagged[i+1] = temp
                        
            self.create_stem(flagged[0].pitch, flagged[count-1].pitch)

            
            if flagged[0].pitch > 5:
                self.create_flag(flagged[0].pitch, flagged[0].pitch - 4, flagged[0].duration)
                
            elif flagged[count - 1].pitch < 11:
                self.create_flag(flagged[count-1].pitch, flagged[count-1].pitch + 4, flagged[count-1].duration)
            
            else:
                self.create_flag(flagged[0].pitch, 0, flagged[0].duration)
                    
        for note in beamed:
            for beam in self.beams:
                if note in beam.notes:
                    self.create_stem(beam.pitch, note.pitch)
    

    def create_stem(self, head, peak):
        if peak > head:
            temp = peak
            peak = head
            head = temp + 1
        for k in range(peak, head):
            if self.rows[k][3] not in {"@","(",")","O","="}:
                self.rows[k][3] = "|"
                
                
    def create_flag(self, head, peak, duration): 
        if peak < head: a = 1                           # stem points up
        else: a = -1                                    # stem points down
        
        self.create_stem(head, peak)
        
        if duration == 1/8:
            if a == 1:
                self.rows[peak]    [3]  = "\\"
                self.rows[peak + 1][4]  = "\\"
                self.rows[peak + 2][4]  = "/"
            else:
                self.rows[peak - 2][4]  = "\\"
                self.rows[peak - 1][4]  = "/"
                self.rows[peak]    [3]  = "/"
                
        elif duration == 1/16:
            if a == 1:
                self.rows[peak]    [3] = "\\"
                self.rows[peak + 1][4] = "\\"
                self.rows[peak + 2][4] = "\\"
                self.rows[peak + 3][4] = "/"
            else:
                self.rows[peak - 3][4]  = "\\"
                self.rows[peak - 2][4]  = "/"
                self.rows[peak - 1][4]  = "/"
                self.rows[peak]    [3]  = "/"
        
        
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
                        
                        
    def create_rests(self):
        for rest in self.rests:
            if rest.duration ==         4:
                self.rows[4] = "--##--"
                self.rows[5] = "  ##  "
                self.rows[6] = "--##--"
                self.rows[7] = "  ##  "
                self.rows[8] = "--##--"
            elif rest.duration ==       2:
                self.rows[4] = "--##--"
                self.rows[5] = "  ##  "
                self.rows[6] = "--##--"
            elif rest.duration ==       1:
                self.rows[4] = "-####-"
                self.rows[5] = " #### "
            elif rest.duration ==       1/2:
                self.rows[5] = " #### "
                self.rows[6] = "-####-"
            elif rest.duration ==       1/4:
                self.rows[4] = "--\---"
                self.rows[5] = "  //  "
                self.rows[6] = "--\---"
                self.rows[7] = "  C   "
            elif rest.duration ==       1/8:
                self.rows[5] = "  @^/ "
                self.rows[6] = "---/--"
                self.rows[7] = "  /   "
            elif rest.duration ==       1/16:
                self.rows[5] = "  @^/ "
                self.rows[6] = "---/--"
                self.rows[7] = "@^/   "
                self.rows[8] = "-/----"
            elif rest.duration ==       1/32:
                self.rows[5]  = " @^|  "
                self.rows[6]  = "---|--"
                self.rows[7]  = " @^|  "
                self.rows[8]  = "---|--"
                self.rows[9]  = " @^|  "
                self.rows[10] = "---|--"
