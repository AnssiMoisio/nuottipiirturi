class Note(object):
    
    ''' Pitch. Numbers are same in Column.rows '''
    
    a2 = 0      # 
    g1 = 1      #                                               |
    f1 = 2      # ------------------------------------\----|----|----------|----------------------------------------------------
    e1 = 3      #                                |    |\   |    |          | ().                                                
    d1 = 4      # -------------------------------|----|\---|---OO----|-----|--|----|-------------------------------\------####--
    c1 = 5      #                                |    |/   |   OO    |     |  |    |    @^/   @^/    @|     \^@    //     ####  
    b1 = 6      # ---------------=======---------|---@@ ---|---OO----|-----|--|----|-----/-----/------|------\-----\------------
    a1 = 7      #                |     |        OO         |         | ____|_____  |    /   @^/      @|       \    C            
    G = 8       # ---\-----------|-----|-------------------|--------OO/----|-----\@@---------/--------|-------------------------
    F = 9       #    |\          |    @@.                  |               |                         @|                         
    E = 10      # ---|/---------@@.------------------------|---------------|--------------------------|-------------------------
    D = 11      #    |
    C = 12      # #-@@-
    B = 13      #
    A = 14      #
    SYL = 15    #   Hel   -  lo     wo  -    rld
        
    
    def __init__(self, pitch, octave, flat, sharp, measure, start, duration):
        self._set_pitch(pitch)
        self.octave = octave
        if flat: self.flat = True
        else: self.flat = False
        if sharp: self.sharp = True
        else: self.sharp = False
        self.measure = measure
        self._set_start(start)
        self._set_duration(duration)
        
        
    def _set_pitch(self, pitch):
        self.pitch = pitch
        
    def _set_start(self, start):
        self.start = start
        
    def _set_duration(self, duration):
        self.duration = duration