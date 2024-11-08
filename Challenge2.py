class HauntedMansion:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __getattr__(self, name):
        return "Booooo, only ghosts here!"
    
    def __setattr__(self, name, value):
        name = f"spooky_{name}"
        super().__setattr__(name, value)