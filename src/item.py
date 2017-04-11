class Item(object):
    
    ''' Pitch. Numbers are same in Column.rows '''
    
    F = 0       #-----------------------------------\----|----|------|------
    E = 1       #                                   |\   |    |      | ().
    D = 2       #-----------------------------------|\---|---()------|------
    C = 3       #                         ======    |    |   ()    | |
    B = 4       #-------------------------|----|---@@ ---|---()----|-|------
    A = 5       #               =======   |   @@         |         | |
    G = 6       #-----======----|-----|--@@--------------|--------()-|------
    f1 = 7      #     |    |    |    @@                  |           |
    e1 = 8      #-----|----|---@@------------------------|-----------|------
    d1 = 9      #     | # @@
    c1 = 10     #    @@
    
    
    ''' Item type'''
    NOTE            = 12
    REST            = 13
    LYRICSYLLABLE   = 14
    
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