class Beam(object):
    
    def __init__(self, notes):
        self.notes = notes
        self.measure = notes[0].measure
        self.sort_notes()
        self.add_pitch()
        self.add_start()
        self.add_end()
        
        
    def sort_notes(self):
        count = len(self.notes)
        for i in range(count - 1):                                       #sort notes from lowest to highest
            for i in range(count - 1):
                if self.notes[i].pitch > self.notes[i+1].pitch:
                    temp = self.notes[i]
                    self.notes[i] = self.notes[i+1]
                    self.notes[i+1] = temp
        
        
    def add_pitch(self):
        sum = 0
        a = False
        b = False
        for note in self.notes:
            if note.pitch < 5:
                if note.pitch == 0:
                    b = True
                a = True
                break
            sum += note.pitch - 5
        if not a:
            pitch = int(sum / len(self.notes))
            self.pitch = pitch
        
        if b:
            self.pitch = 14
        elif a:
            self.pitch = 0

    
    
    def add_start(self):
        ref = 1
        for note in self.notes:
            if note.start < ref:
                ref = note.start
        self.start = ref
        
        
    def add_end(self):
        ref = 0
        for note in self.notes:
            if note.start > ref:
                ref = note.start
        self.end = ref