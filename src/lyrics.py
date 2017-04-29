class Lyrics(object):
    
    def __init__(self, measure, start, string):
        self._set_measure(measure)
        self._set_start(start)
        self.string = string
        
        
    def _set_start(self, start):
        self.start = start
        
    def _set_measure(self, measure):
        self.measure = measure