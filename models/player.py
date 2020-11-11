import numpy as np


class Player():

    player_type = "FOOTBALL"

    def __init__(self, firstname, lastname, position, age, team):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.age = age
        self.team = team

    def __str__(self):
        return self.firstname + " " + self.lastname

    def getPositions(self):
        return self.position

    def getTeam(self):
        return self.team

    def getAge(self):
        return self.age

class Quarterback(Player):

    def __init__(self, **kwargs):
        defaults = {
            "firstname": "first",
            "lastname": "last",
            "position": "NA",
            "age": 18,
            "team": "None",
            "games": 0,
            "pass_att": 0,
            "comp_per": 0,
            "pass_yards": 0,
            "pass_tds": 0,
            "pass_ints": 0,
            "qb_rate": 0,
            "sacks": 0,
            "sack_yards": 0,
            "rush_att": 0,
            "rush_yards": 0,
            "rush_tds": 0,
            "fumbles": 0,
            "num_snaps": 0
        }

        if not bool(kwargs.items()):
            for k, v in defaults.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return super.__str__(self)

    def calc_fantasy_pts(self, league_scoring_format):
        return self.pass_yards

class RunningBack(Player):

    def __init__(self, **kwargs):
        defaults = {
            "firstname": "first",
            "lastname": "last",
            "position": "RB",
            "age": 18,
            "team": "None",
            "games": 0,
            "rush_att": 0,
            "rush_yards": 0,
            "rush_tds": 0,
            "targets": 0,
            "receptions": 0,
            "rec_yards": 0,
            "rec_tds": 0,
            "fumbles": 0,
            "num_snaps": 0
        }

        if not bool(kwargs.items()):
            for k, v in defaults.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return super.__str__(self)

    def calc_fantasy_pts(self, league_scoring_format):
        return self.rush_yards

class WideReciever(Player):

    def __init__(self, **kwargs):
        defaults = {
            "firstname": "first",
            "lastname": "last",
            "position": "WR",
            "age": 18,
            "team": "None",
            "targets": 0,
            "receptions": 0,
            "rec_yards": 0,
            "rec_tds": 0,
            "fumbles": 0,
            "games": 0,
            "rush_att": 0,
            "rush_yards": 0,
            "rush_tds": 0,
            "num_snaps": 0
        }

        if not bool(kwargs.items()):
            for k, v in defaults.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return super.__str__(self)

    def calc_fantasy_pts(self, league_scoring_format):
        return self.rec_yards

class TightEnd(Player):

    def __init__(self, **kwargs):
        defaults = {
            "firstname": "first",
            "lastname": "last",
            "position": "TE",
            "age": 18,
            "team": "None",
            "targets": 0,
            "receptions": 0,
            "rec_yards": 0,
            "rec_tds": 0,
            "fumbles": 0,
            "games": 0,
            "rush_att": 0,
            "rush_yards": 0,
            "rush_tds": 0,
            "num_snaps": 0
        }

        if not bool(kwargs.items()):
            for k, v in defaults.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return super.__str__(self)

    def calc_fantasy_pts(self, league_scoring_format):
        return self.rec_yards

class Kicker(Player):

    def __init__(self, **kwargs):
        defaults = {
            "firstname": "first",
            "lastname": "last",
            "position": "TE",
            "age": 18,
            "team": "None",
            "extra_pts": 0,
            "fg_30": 0,
            "fg_40": 0,
            "fg_50": 0,
            "fg_60": 0
        }

        if not bool(kwargs.items()):
            for k,v in defaults.items():
                setattr(self, k, v)
        else:
            for k,v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        return super.__str__(self)

    def calculate_fantasy_pts(elf, league_scoring_format):
        return self.extra_pts * 3



