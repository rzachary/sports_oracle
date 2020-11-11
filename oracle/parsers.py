import csv
import json
import datetime
from pymongo import MongoClient, errors

# Parses csv and json and yaml files to fill data for players, teams, and games

# header information for new json file
header = ['name','dob', 'position', 'team', 'college', 'draft_year', 'year_start', 'year_end',
          'height', 'weight']
players = {}
key = 0
ip_addr = '127.0.0.1'
port = 27017
filename = '../data/football/raw_all_players.csv'

# Open the csv file containing the raw data
with open(filename, encoding='utf-8') as csvfile:

    playerreader = csv.DictReader(csvfile)

    line = []
    newline = []

    for rows in playerreader:
        key = key + 1
        # for some reason heights are being seen as dates '%d-%b -> %m-%d'
        fix_height = rows['height']
        if fix_height != '6-0':
            rows['height'] = fix_height[::-1]
        players[key] = rows
    print(players)


# create connection to the MongoDB database
try:
    client = MongoClient(
        host = [ str(ip_addr) + ":" + str(port) ],
        serverSelectionTimeoutMS = 3000,
        username = 'local',
        password = 'local',
    )

    print ("connect to server:", client.server_info()["version"])

    # pull up players collection and fill it with player data
    db = client['players']
    collections = db['players']

    collection.Insert(players)

except errors.ServerSelectionTimeOutError as err:
    # set the client and DB name list to nothing
    client = None

    print ("pymongo ERROR:", err)

print("Completed filling Players Database.")
