class ProtectedSection:
    def __init__(self, log=(), suppress=()):
        self.log_errors = log
        self.suppress_errors = suppress
        self.exception = None
        
    def __enter__(self):
       return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return False
        
        for error in self.log_errors:
            if exc_type == error:
                self.exception = exc_val
                return True

        for error in self.suppress_errors:
            if exc_type == error:
                return True 
        return False