class TextFileIO(object):
    
    def load_composition(self, filename):
        
        file = open(filename, "r")
        
        for line in file.readlines():
            print(line)