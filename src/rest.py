class Rest:
    
    def __init__(self, measure, start, duration):
        self._set_measure(measure)
        self._set_start(start)
        self._set_duration(duration)
        
    def _set_start(self, start):
        self.start = start
        
    def _set_duration(self, duration):
        self.duration = duration
        
    def _set_measure(self, measure):
        self.measure = measure
        