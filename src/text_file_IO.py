from corrupted_composition_file_error import *
from composition import Composition
from note import Note
from rest import Rest
from char_graphics import CharGraphics

class TextFileIO(object):

    def __init__(self):
        self.comp = None
        self.keyboard_input()
        
        
    def keyboard_input(self):
        self.file_name = input("Anna savellystiedoston nimi\n")
        self.read_file()
        mode = input("Lisaa tai poista nuotti, tauko, sanoitus, palkki? Poistu: esc\n")
        line = None
        while mode != "esc":
            if mode.lower().strip() == "lisaa nuotti":
                line = input("syntaksi: korkeus, oktaavi, alennus k/e, ylennys k/e, tahti, aloitushetki, kesto\n")
                self.parse_nuotit(line)
                
            # implement allllllll the rest
            CharGraphics(self.comp)
            mode = input("Lisaa tai poista nuotti, tauko, sanoitus, palkki? Poistu: esc\n")
    
    
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
        
        file.close()
        self.comp.fill_holes()
        CharGraphics(self.comp)
        print(self.comp.rests)
                    
                    
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
                start = float(int(start[0].strip()) / int(start[1].strip()))                # start
                duration = parts[6].split("/")
                duration = float(int(duration[0].strip()) / int(duration[1].strip()))       # duration
                
                note = Note(pitch, octave, flat, sharp, measure, start, duration)
                Composition.add_note(self.comp, note)
                  
            else: 
                raise CorruptedCompositionFileError("Outo savelkorkeus")
            
            
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
    
        
        
        
        
        
        
        
        