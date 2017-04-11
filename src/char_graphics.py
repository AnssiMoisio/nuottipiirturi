from item import Item
from composition import Composition
from column import Column

class CharGraphics(object):
    
    def __init__(self, composition):
        self.columns = []         # list of Column objects
        #self.sheet = []
        self.create_columns(composition)
        self.sheet()
        
    def create_columns(self, composition):
        col = Column(composition, 0, 0)
        self.columns.append(col)
        col = Column(composition, 0, 1)
        self.columns.append(col)
        
            
    def sheet(self):
        '''
        Creates a matrix from columns array,
        containing all columns, the whole sheet music (and prints it?)
        '''
        
        
        for k in range(10):
            #for i in range(len(self.columns)):
            print(self.columns[0].rows[k] + self.columns[1].rows[k])
                    
    
    #def print_sheet(self):