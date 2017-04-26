from note import Note
from rest import Rest
from beam import Beam
from composition import Composition
from char_graphics import CharGraphics
from text_file_IO import TextFileIO

import unittest
from io import StringIO

class Test(unittest.TestCase):
    
    def setUp(self):
        self.human_IO = TextFileIO()
        
        
    def test_example(self):
        '''skip'''

if __name__ == '__main__':
    unittest.main()