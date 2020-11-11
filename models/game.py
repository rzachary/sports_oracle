import numpy as np


class Game():

    def __init__(self, **kwargs):
        defaults = {

        }

         if not bool(kwargs.items()):
            for k, v in defaults.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return "This is a game"

