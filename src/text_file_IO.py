from corrupted_composition_file_error import *
from composition import Composition
from note import Note
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
            mode = input("Lisaa tai poista nuotti, tauko, sanoitus, palkki?\n poistu: esc\n")
    
    
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
                        self.comp = Composition(name, creator, meter, length)   # Creating the composition object
                        
                if not current_line == None:
                    if current_line[1:7].lower() == 'nuotit':
                        for line in file:
                            self.parse_nuotit(line)
        
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
        
        
        
        current_line = line
        if current_line != None:
            
            parts = current_line.split(",")
            
            if parts[0].strip().lower() in {"a","b","c","d","e","f","g"}:
                if int(parts[1].strip()) == 0:
                    octave = 0
                elif int(parts[1].strip()) == 1:
                    octave = 1
                else: raise CorruptedCompositionFileError("Outo oktaavi")
                if octave == 0:
                    A = Note.A
                    B = Note.B
                    C = Note.C
                    D = Note.D
                    E = Note.E
                    F = Note.F
                    G = Note.G
                else:
                    A = Note.a1
                    B = Note.b1
                    C = Note.c1
                    D = Note.d1
                    E = Note.e1
                    F = Note.f1
                    G = Note.g1
                if parts[0].strip().lower() == "a":
                    pitch = A
                elif parts[0].strip().lower() == "b":
                    pitch = B
                elif parts[0].strip().lower() == "c":
                    pitch = C
                elif parts[0].strip().lower() == "d":
                    pitch = D
                elif parts[0].strip().lower() == "e":
                    pitch = E
                elif parts[0].strip().lower() == "f":
                    pitch = F
                elif parts[0].strip().lower() == "g":
                    pitch = G
                
                if parts[2].strip().lower() == "k": flat = True
                else: flat = False
                if parts[3].strip().lower() == "k": sharp = True
                else: sharp = False
                
                
                measure = int(parts[4].strip())
                start = parts[5].split("/")
                start = float(int(start[0].strip()) / int(start[1].strip()))
                duration = parts[6].split("/")
                duration = float(int(duration[0].strip()) / int(duration[1].strip()))
                
                print(pitch, octave, flat, sharp, measure, start, duration)
                note = Note(pitch, octave, flat, sharp, measure, start, duration)
                Composition.add_note(self.comp, note)
                  
            elif current_line[0] == '#':
                return current_line
            else: 
                raise CorruptedCompositionFileError("Outo savelkorkeus")
            