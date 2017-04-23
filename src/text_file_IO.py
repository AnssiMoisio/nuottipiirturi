from corrupted_composition_file_error import *
from composition import Composition

class TextFileIO(object):

    def __init__(self):
        self.keyboard_input()
        self.comp = Composition(None, None, 0, 0)       # (name, creator, meter, length)
        
        
    def keyboard_input(self):
        self.file_name = input("Anna savellystiedoston nimi")
        self.read_file()
        mode = input("Lisaa tai poista nuotti, tauko, sanoitus, palkki?")
        if mode.lower() == "lisaa nuotti":
            self.parse_nuotti()
    
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
                    name, creator = self.parse_tiedot(file)
                    self.comp.name = name
                    self.comp.creator = creator
                    
                elif line_parts[0].strip().lower() == '#nuotit':
                    self.parse_nuotit()
                    
    
    def parse_nuotit(self):
        pass