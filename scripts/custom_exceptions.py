class Error(Exception):
    """Base class for exceptions"""
    pass


class ProblemImportError(Error):
    """Exception raised for errors with problem import

    Attributes:
        message -- explanation of error
    """
    def __init__(self, message):
        self.message = message
