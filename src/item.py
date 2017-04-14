class Item(object):
    
    ''' Pitch. Numbers are same in Column.rows '''
    
    a1 = 0      # 
    g1 = 1      #                                              |
    f1 = 2      # -----------------------------------|----|----|----------|-------------
    e1 = 3      #                                    |    |    |          | ().   
    d1 = 4      # -----------------------------------|----|---()----------|--|----|-----
    c1 = 5      #                          ======    |    |   ()    |     |  |    |
    b1 = 6      # -------------------------|----|---@@ ---|---()----|-----|--|----|-----
    A = 7       #                =======   |   @@         |         | ____|_____  |
    G = 8       # -----======----|-----|--@@--------------|--------()/----|-----\@@-----
    F = 9       #      |    |    |    @@                  |               |
    E = 10      # -----|----|---@@------------------------|---------------|-------------
    D = 11      #      | # @@
    C = 12      #   -@@-
    B = 13      #
        
    
    ''' Item type'''
    NOTE            = 22
    REST            = 33
    LYRICSYLLABLE   = 44
    
    def __init__(self, item_type, pitch, measure, start, duration):
        self._set_type(item_type)
        self._set_pitch(pitch)
        self.measure = measure
        self._set_start(start)
        self._set_duration(duration)
        
    def _set_type(self, item_type):
        if item_type in [Item.NOTE, Item.REST, Item.LYRICSYLLABLE]:
            self.item_type = item_type
        else:
            raise ValueError("Bad item type given")
        
    def _set_pitch(self, pitch):
        self.pitch = pitch
        
    def _set_start(self, start):
        self.start = start
        
    def _set_duration(self, duration):
        self.duration = duration