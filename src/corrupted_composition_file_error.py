class CorruptedCompositionFileError(Exception):

    def __init__(self, message):
        super(CorruptedCompositionFileError, self).__init__(message)