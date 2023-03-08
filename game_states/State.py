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

# class NewState(State):
#     """
#
#     """
#     def __init__(self):
#         super().__init__()
#         self.next = 
#         self.name = 
#         self.fps = 60

#     def cleanup(self) -> None:
#         """
#         Cleans up the state
#         """    
#     def startup(self):
#         """
#         Initialises the state
#         """

#     def get_event(self, event) -> None:
#         """
#         Event listener
#         """

#     def update(self, screen) -> None:
#         """
#         Non event loop logic
#         """
#         self.draw(screen)

#     def draw(self, screen) -> None:
#         """
#         Graphics
#         """