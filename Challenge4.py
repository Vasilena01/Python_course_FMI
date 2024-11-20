class LockPicker_4MI0600290:
    def __init__(self, lock):
        self.lock = lock
    
    def unlock(self):
        args_count = self._get_args_count()
        args = [None] * args_count
        
        while True:
            try:
                self.lock.pick(*args)
                return
            except TypeError as exc:
                    if exc.position is not None:
                        args[exc.position - 1] = exc.expected()
            except ValueError as exc:
                    if exc.position is not None:
                        args[exc.position - 1] = exc.expected 
    
    def _get_args_count(self):
        try:
            self.lock.pick()
        except TypeError as exc:
            if exc.position is None:
                return exc.expected
        return 0