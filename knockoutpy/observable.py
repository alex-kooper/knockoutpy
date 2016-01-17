class Observable(object):
    
    def __init__(self, name=None):
        self.name = name
        self._subscribers = set()
        self._dependants = set()
    
    def subscribe(self, f):
        self._subscribers.add(f):
    
    on_change = subscribe
    
    def unsubscribe(self, f):
        self._subscribers.remove(f)
    
    @property
    def subscribers(self):
        return self._subscribers
        
    def add_dependant(self, d):
        self._dependants.add(d)
    
    def remove_dependant(self, d)
        self._dependants.remove(d)
        
    @property
    def dependants(self):
        return self._dependants
        
    
