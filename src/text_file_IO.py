from corrupted_composition_file_error import *
from composition import Composition
from note import Note
from rest import Rest
from beam import Beam
from char_graphics import CharGraphics

class TextFileIO(object):

    def __init__(self):
        self.comp = None
        self.keyboard_input()
        
        
    def keyboard_input(self):
        self.file_name = input("Anna savellystiedoston nimi\n")
        self.read_file()
        mode = input("Lisaa tai poista nuotti/tauko/palkki? Sulje ohjelma: quit\n")
        line = None
        while mode != "quit":
            if mode.lower().strip() == "lisaa nuotti":
                line = input("syntaksi: korkeus, oktaavi, alennus k/e, ylennys k/e, tahti, aloitushetki, kesto\nTulosta: esc\n")
                while (1):
                    if line.strip() == "esc": break
                    self.parse_nuotit(line)
                    line = input()
                
            elif mode.lower().strip() == "poista nuotti":
                line = input("syntaksi: tahti, <jarjestysnumero nuotille, aloitushetken; korkeuden mukaan>\nesim: 1,2\nPoistu ja tulosta: esc\n")
                while (1):
                    if line.strip() == "esc": break
                    try:
                        self.remove_note(line)
                    except ValueError:
                        print("Talla jarjestysnumerolla ei ole nuottia. Numerointi alkaa luvusta 0.")
                            
                    line = input()
            
            elif mode.lower().strip() == "lisaa tauko":
                line = input("syntaksi: tahti, aloitushetki, kesto\nPoistu ja tulosta: esc\n")
                while (1):
                    if line.strip() == "esc": break
                    self.parse_tauot(line)
                    line = input()
                        
            elif mode.lower().strip() == "poista tauko":
                line = input("syntaksi: tahti, aloitushetki\nesim: 1,3/8\nPoistu ja tulosta: esc\n")
                while (1):
                    if line.strip() == "esc": break
                    self.remove_rest(line)
                    line = input()
                        
            elif mode.lower().strip() == "lisaa palkki":
                line = input("syntaksi:tahti, <jarjestysnumero nuotille, aloitushetken; korkeuden mukaan>\nPoistu ja tulosta: esc\n")
                while (1):
                    if line.strip() == "esc": break
                    try:
                        self.parse_palkit(line)
                    except ValueError:
                        print("Talla jarjestysnumerolla ei ole nuottia. Numerointi alkaa luvusta 0.")
                    line = input()
                        
            elif mode.lower().strip() == "poista palkki":
                line = input("syntaksi: tahti, aloitushetki\nesim: 1,3/8\nPoistu ja tulosta: esc\n")
                while(1):
                    if line.strip() == "esc": break
                    self.remove_beam(line)
                    line = input()
                
            self.comp.fill_holes()
            CharGraphics(self.comp)
            mode = input("Lisaa tai poista nuotti/tauko/palkki? Sulje ohjelma: quit\n")
    
    
    def read_file(self):

        file = open(self.file_name, "r")
        
        current_line = file.readline()
        header_parts = current_line.split(" ")

        if header_parts[0] != "SAVELLYS":
            raise CorruptedCompositionFileError("Unknown file type")

        if header_parts[2].strip().lower() != 'tallennustiedosto':
            raise CorruptedCompositionFileError("Unknown file type")
        
        for line in file:
            current_line = line
            
            if current_line[0] == "#":
                line_parts = current_line.split(" ")
                
                if line_parts[0].strip().lower() == '#tiedot':
                    if self.comp != None:
                        raise CorruptedCompositionFileError("Monta tietoa")
                    else:
                        name, creator, meter, length, current_line = self.parse_tiedot(file)
                        self.comp = Composition(name, creator, meter, length)                   # Creating the composition object
                        
                if not current_line == None:
                    if current_line[1:7].lower() == 'nuotit':
                        for line in file:
                            if line[0] == "#":
                                current_line = line
                                break
                            self.parse_nuotit(line)
                       
                    if current_line[1:6].lower() == 'tauot':
                        for line in file:
                            if line[0] == "#":
                                current_line = line
                                break
                            current_line = self.parse_tauot(line)
                            
                    if current_line[1:7].lower() == 'palkit':
                        for line in file:
                            if line[0] == "#":
                                current_line = line
                                break
                            current_line = self.parse_palkit(line)
        
        file.close()
        self.comp.fill_holes()
        CharGraphics(self.comp)
                    
                    
    def parse_tiedot(self, input):
        creator = None
        name = None
        meter = None
        length = 0
        
        for line in input:
            line_parts = line.split(":")
            
            if line_parts[0].strip().lower() == 'tekija':
                creator = line_parts[1].strip()
                
            elif line_parts[0].strip().lower() == 'nimi':
                name = line_parts[1].strip()
                
            elif line_parts[0].strip().lower() == 'tahtilaji':
                meter = line_parts[1].strip()
                
            elif line_parts[0].strip().lower() == 'pituus':
                length = int( line_parts[1].strip() )
                
            if line[0] == '#':
                return name, creator, meter, length, line
                
        return name, creator, meter, length, line
            
            
    def parse_nuotit(self, line):
        '''(pitch, octave, flat, sharp, measure, start, duration)'''
        
        if line.strip() != "":
            parts = line.split(",")
            if parts[0].strip().lower() in {"a","b","c","d","e","f","g"}:                  
                if parts[0].strip().lower() == "a":
                    pitch = Note.A
                elif parts[0].strip().lower() == "b":
                    pitch = Note.B
                elif parts[0].strip().lower() == "c":
                    pitch = Note.C
                elif parts[0].strip().lower() == "d":
                    pitch = Note.D
                elif parts[0].strip().lower() == "e":
                    pitch = Note.E
                elif parts[0].strip().lower() == "f":
                    pitch = Note.F
                elif parts[0].strip().lower() == "g":
                    pitch = Note.G
                
                if int(parts[1].strip()) in {0,1,2}:
                    octave = int(parts[1].strip())
                else: raise CorruptedCompositionFileError("Outo oktaavi")
                pitch =  pitch - (octave*7)                                                 # pitch
                
                if parts[2].strip().lower() == "k": flat = True                             # flat
                else: flat = False
                if parts[3].strip().lower() == "k": sharp = True                            # sharp
                else: sharp = False
                
                measure = int(parts[4].strip())                                             # measure
                start = parts[5].split("/")
                if len(start) == 1:
                    start = float(start[0].strip())
                elif len(start) == 2:
                    start = float(int(start[0].strip()) / int(start[1].strip()))
                else:
                    raise CorruptedCompositionFileError("Huono alkamishetki.")
                duration = parts[6].split("/")
                if len(duration) == 1:
                    duration = float(duration[0].strip())
                elif len(duration) == 2:
                    duration = float(int(duration[0].strip()) / int(duration[1].strip()))
                else:
                    raise CorruptedCompositionFileError("Huono kesto")
                
                note = Note(pitch, octave, flat, sharp, measure, start, duration)
                Composition.add_note(self.comp, note)
                  
            else: 
                raise CorruptedCompositionFileError("Outo savelkorkeus")
            
    def remove_note(self, line):
        if line.strip() != "":
            parts = line.split(",")
            measure = int(parts[0].strip())
            measurenotes = self.sort_measurenotes(measure)
            
            try:
                notesort = int(parts[1].strip())
            except ValueError:
                print("Huono nuotti. Yrita uudestaan.")
            try:
                note = measurenotes[notesort]
                Composition.remove_note(self.comp, measure, note.start, note.pitch)
            except IndexError:
                print("talla jarjestysluvulla ei ole nuottia. Numerointi alkaa luvusta 0. Yrita uudestaan tai poistu komennolla esc.")
                
    def remove_rest(self, line):
        if line.strip() != "":
            parts = line.split(",")
            measure = int(parts[0].strip())
            start = parts[1].split("/")
            if len(start) == 1:
                start = float(start[0].strip())
            elif len(start) == 2:
                start = float(int(start[0].strip()) / int(start[1].strip()))
            else:
                raise CorruptedCompositionFileError("Huono alkamishetki.")
            
            for rest in self.comp.rests:
                if rest.start == start and rest.measure == measure:
                    Composition.remove_rest(self.comp, measure, start)
                    
    def remove_beam(self, line):
        if line.strip() != "":
            parts = line.split(",")
            measure = int(parts[0].strip())
            start = parts[1].split("/")
            if len(start) == 1:
                start = float(start[0].strip())
            elif len(start) == 2:
                start = float(int(start[0].strip()) / int(start[1].strip()))
            else:
                raise CorruptedCompositionFileError("Huono alkamishetki.")
            
            for beam in self.comp.beams:
                if beam.start == start and beam.measure == measure:
                    Composition.remove_beam(self, measure, start)
            
            
    def parse_tauot(self, line):
        if line.strip() != "":
            parts = line.split(",")
            measure = int(parts[0].strip())                                             # measure
            start = parts[1].split("/")
            start = float(int(start[0].strip()) / int(start[1].strip()))                # start
            duration = parts[2].split("/")
            if len(duration) == 1:
                duration = float(duration[0].strip())
            elif len(duration) == 2:
                duration = float(int(duration[0].strip()) / int(duration[1].strip()))
            else:
                raise CorruptedCompositionFileError("Huono kesto")
            
            rest = Rest(measure, start, duration)
            Composition.add_rest(self.comp, rest)
            
            
    def sort_measurenotes(self, measure):
        '''Returns a list of notes in this measure, sorted'''
        
        measurenotes = []
        
        for note in self.comp.notes:
            if note.measure == measure:
                measurenotes.append(note)
        
        count = len(measurenotes)
        for i in range(count - 1):                     # sort notes from first to last start and lowest to highest pitch
            for i in range(count - 1):
                if measurenotes[i].start > measurenotes[i+1].start:
                    temp = self.comp.notes[i]
                    measurenotes[i] = measurenotes[i+1]
                    measurenotes[i+1] = temp
                    
                elif measurenotes[i].start == measurenotes[i+1].start and measurenotes[i].pitch > measurenotes[i+1].pitch:
                    temp = self.comp.notes[i]
                    self.comp.notes[i] = self.comp.notes[i+1]
                    self.comp.notes[i+1] = temp
        
        return measurenotes
            
            
    def parse_palkit(self, line):
        if line.strip() != "":
            parts = line.split(",")
            measure = int(parts[0].strip())
            measurenotes = self.sort_measurenotes(measure)
            notes = []
                
            note_parts = parts[1].split(":")
            for note in note_parts:
                try:
                    notesort = int(note.strip())
                except ValueError:
                    raise CorruptedCompositionFileError("Omituinen nuotti palkille")
                
                notes.append(measurenotes[notesort])
                
        beam = Beam(notes)
        Composition.add_beam(self.comp, beam)
                    
            
                
                
        