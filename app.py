from typing import Tuple
from flask import Flask
from flask_cors import CORS, cross_origin
import pandas
import json

#insert the cors header per usual

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return 'Index Page'

@app.route('/api/v1/wednesday/teams/roster')
def parse():
    data = {}
    data["Bruins"] = []
    data["Devils"] = []
    data["Flyers"] = []
    data["Rangers"] = []
    df = pandas.read_csv("data/Wednesday.csv")
    for i in df["Bruins"]:
        if not pandas.isnull(i):
            data["Bruins"].append(i)
    for i in df["Rangers"]:
        if not pandas.isnull(i):
            data["Rangers"].append(i)
    for i in df["Flyers"]:
        if not pandas.isnull(i):
            data["Flyers"].append(i)
    for i in df["Devils"]:
        if not pandas.isnull(i):
            data["Devils"].append(i)
        
    return json.dumps(data, indent=2)

@app.route('/api/v1/wednesday/teams/standings')
def get_standings():
    df = pandas.read_csv("data/Wednesday.csv")
    df = df.iloc[0:4, 4:8]
    standings = []
    for i, row in df.iterrows():
        team = {}
        team["Team"] = row["Standings"]
        team["Wins"] = row["Wins"]
        team["Loses"] = row["Loses"]
        team["Ties"] = row["Ties"]
        standings.append(team)

    return json.dumps(standings, indent=2)

@app.route('/api/v1/wednesday/teams/schedule')
def get_schedule():
    df = pandas.read_csv("data/Wednesday.csv")
    df = df.iloc[0:23, 8:12]
    schedule = []
    for i, row in df.iterrows():
        t = (row["Game Week"], row["Date"], row["Away"], row["Home"])
        schedule.append(t) 
        t = ()
    return json.dumps(schedule, indent=2)

@app.route('/api/v1/friday/teams/roster')
def get_friday_roster():
    data = {}
    data["Muffins"] = []
    data["Bagels"] = []
    data["Coffee"] = []
    data["Hawks"] = []
    df = pandas.read_csv("data/Friday.csv")
    for i in df["Muffins"]:
        if not pandas.isnull(i):
            data["Muffins"].append(i)
    for i in df["Bagels"]:
        if not pandas.isnull(i):
            data["Bagels"].append(i)
    for i in df["Coffee"]:
        if not pandas.isnull(i):
            data["Coffee"].append(i)
    for i in df["Hawks"]:
        if not pandas.isnull(i):
            data["Hawks"].append(i)
        
    return json.dumps(data, indent=2)

@app.route('/api/v1/friday/teams/standings')
def get_friday_standings():
    df = pandas.read_csv("data/Friday.csv")
    df = df.iloc[0:4, 4:8]
    standings = []
    for i, row in df.iterrows():
        team = {}
        team["Team"] = row["Standings"]
        team["Wins"] = row["W"]
        team["Loses"] = row["L"]
        team["Ties"] = row["Ties"]
        standings.append(team)

    return json.dumps(standings, indent=2)

@app.route('/api/v1/friday/teams/schedule')
def get_friday_schedule():
    df = pandas.read_csv("data/Friday.csv")
    df = df.iloc[0:23, 8:12]
    schedule = []
    for i, row in df.iterrows():
        t = (row["Game Week"], row["Date"], row["Away"], row["Home"])
        schedule.append(t) 
        t = ()
    return json.dumps(schedule, indent=2)
