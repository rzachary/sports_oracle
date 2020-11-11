import numpy as np
# import sklearn
import requests

# hold the data to assist in the simulation for a season
class Season():

    num_of_games = 16

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
        return "This is a season"
