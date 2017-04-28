from corrupted_composition_file_error import *
from composition import Composition
from note import Note
from rest import Rest
from beam import Beam
from char_graphics import CharGraphics
from fractions import Fraction

class TextFileIO(object):

    def __init__(self):
        self.comp = None
        self.commentblock = "\n#KOMMENTIT\n"
        self.keyboard_input()
        
        
        
    def keyboard_input(self):
        self.file_name = input("Anna savellystiedoston nimi\n")
        self.read_file()
        mode = input("Lisaa tai poista nuotti/tauko/palkki? 'lisaa nuotti'\nTayta tyhjat kohdat tauoilla: 'tayta'\n'tallenna'\nSulje ohjelma: 'quit'\n")
        line = None
        while mode != "quit":
            
            if mode.lower().strip() == "tallenna":
                self.write_file()
            
            elif mode.lower().strip() == "lisaa nuotti":
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
                        if self.remove_note(line):
                            print("Nuotti poistettu. Anna seuraava poistettava nuotti tai poistu komennolla esc")
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
                
            elif mode.lower().strip() == "tayta":
                self.comp.fill_holes()
                
            
            CharGraphics(self.comp)
            mode = input("Anna komento\n")
    
    
    def read_file(self):

        file = open(self.file_name, "r")
        
        current_line = file.readline()
        self.header = current_line
        header_parts = current_line.split(" ")

        if header_parts[0] != "SAVELLYS":
            raise CorruptedCompositionFileError("Unknown file type")

        if header_parts[2].strip().lower() != 'tallennustiedosto':
            raise CorruptedCompositionFileError("Unknown file type")
        
        for line in file:
            ref = False
            count = 0
            while line[0] == "#" or ref:
                count += 1
                if count > 10: break
                
                if line[1:7].lower() == 'tiedot':
                    if self.comp != None:
                        raise CorruptedCompositionFileError("Monta tietoa")
                    else:
                        name, creator, meter, length, line = self.parse_tiedot(file)
                        self.comp = Composition(name, creator, meter, length)                   # Creating the composition object
                        
                if line[1:10].lower() == 'kommentit':
                    
                    for line in file:
                        if line[0] == "#":
                            ref = True
                            break
                        else:
                            ref = False
                            self.commentblock = self.commentblock + line
                        
                elif line[1:7].lower() == 'nuotit':
                    for line in file:
                        if line[0] == "#":
                            ref = True
                            break
                        else:
                            ref = False
                            self.parse_nuotit(line)
                   
                elif line[1:6].lower() == 'tauot':
                    for line in file:
                        if line[0] == "#":
                            ref = True
                            break
                        else:
                            ref = False
                            self.parse_tauot(line)
                        
                elif line[1:7].lower() == 'palkit':
                    for line in file:
                        if line[0] == "#":
                            ref = True
                            break
                        else:
                            ref = False
                            self.parse_palkit(line)
                            
                elif line[1:9].lower() == 'sanoitus':
                    for line in file:
                        if line[0] == "#":
                            ref = True
                            break
                        else:
                            ref = False
                            self.parse_sanoitus(line)
                    
        
        file.close()
        CharGraphics(self.comp)
    
        
    def write_file(self):
        
        asd = self.header
        asd = asd + "\n#TIEDOT\n"
        asd = asd +  "nimi: " + self.comp.name + "\ntekija: " + self.comp.creator + "\npituus: " + str(self.comp.length) + "\ntahtilaji: " + self.comp.meter + "\n"
        asd = asd + self.commentblock
        asd = asd + "\n#NUOTIT\n"
        for note in self.comp.notes:
            if note.pitch + (note.octave*7) == Note.A:
                a = "A"
            elif note.pitch + (note.octave*7) == Note.B:
                a = "B"
            elif note.pitch + (note.octave*7) == Note.C:
                a = "C"
            elif note.pitch + (note.octave*7) == Note.D:
                a = "D"
            elif note.pitch + (note.octave*7) == Note.E:
                a = "E"
            elif note.pitch + (note.octave*7) == Note.F:
                a = "F"
            elif note.pitch + (note.octave*7) == Note.G:
                a = "G"
            b = str(note.octave)
            if note.flat: c = "k"
            else: c = "e"
            if note.sharp: d = "k"
            else: d = "e"
            e = str(note.measure)
            fract = Fraction(note.start)
            f = str(fract.numerator) + "/" + str(fract.denominator)
            if note.duration < 1:
                g = "1/" + str(int(1/note.duration))
            else: g = str(note.duration)
            asd = asd + a+", "+b+", "+c+", "+d+", "+e+", "+f+", "+g+"\n"
            
        asd = asd + "\n#TAUOT\n"    
        
        for rest in self.comp.rests:
            e = str(rest.measure)
            fract = Fraction(rest.start)
            f = str(fract.numerator) + "/" + str(fract.denominator)
            if rest.duration < 1:
                g = "1/" + str(int(1/rest.duration))
            else: g = str(rest.duration)
            asd = asd +e+", "+f+", "+g+"\n"
            
        asd = asd + "\n#PALKIT\n"    
            
        for beam in self.comp.beams:
            a = str(beam.measure)
            b = str(self.sort_measurenotes(beam.measure).index(beam.notes[0]))
            for i in range(1,len(beam.notes)):
                b = b + ":" + str(self.sort_measurenotes(beam.measure).index(beam.notes[i]))
            asd = asd + a + ", " + b + "\n"
            
        
        save_file = input("Tallennustiedosto:\n")
        file = open(save_file, "w")
        file.write(asd)
        file.close()
            
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
        
        
    def parse_sanoitus(self, line):
        '''implement'''
        
            
    def remove_note(self, line):
        if line.strip() != "":
            parts = line.split(",")
            measure = int(parts[0].strip())
            measurenotes = self.sort_measurenotes(measure)
            
            try:
                notesort = int(parts[1].strip())
                note = measurenotes[notesort]
                Composition.remove_note(self.comp, measure, note.start, note.pitch)
                return True
            except:
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
                    Composition.remove_beam(self.comp, measure, start)
            
            

            
            
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
            

                    