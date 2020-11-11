import numpy
import csv



class Play():

    def __init__(self, **kwargs):
        defaults = {
            "gameid" : 0,
            "game_date": "1900-01-31",
            "Off_Team": "ATL",
            "Def_Team": "DET",
            "Down": 1,
            "ToGo": 10,
            "YardLine": 20,
            "Description": "TIMEOUT",
            "Away_Win_Pct": 100.0,
            "Home_Win_Pct": 0.0,
            "Year": "1900",
            "Yards": 0.0,
            "Formation": "UNDER CENTER",
            "Play_Type": "TIMEOUT",
            "IsRush": 0,
            "IsIncomplete": 0,
            "IsTouchdown": 0,
            "PassType": "None",
            "IsSack": 0,
            "IsChallenge": 0,
            "IsChallengeReversed": 0,
            "Challenge_Team": "ATL",
            "IsInterception": 0,
            "IsFumble": 0,
            "IsPenalty": 0,
            "IsAccepted": 0,
            "PenaltyTeam": "DET",
            "PenaltyType": "HOLDING",
            "PenaltyYards": 10
        }

        if not bool(kwargs.items()):
            for k,v in defaults.items():
                setattr(k,v,self)
        else:
            for k,v in kwargs.items():
                setattr(k,v,self)


    def __str__(self):
        return self.description

    def export_numpy_array():
        return ""
