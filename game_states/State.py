class State():
    """ 
    Base class for game state
    """
    def __init__(self):
        self.done = False      # is the game state finished
        self.next = None       # which state comes next
        self.previous = 'None' # which state came before
        self.quit = False      # should the game quit
        self.fps = 60          # framerate