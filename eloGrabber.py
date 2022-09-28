#!/usr/bin/env python3
"""analyzes the elo of an event over time"""
from sys import argv
import json
import requests
import datetime
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

argv = argv[1:]
headers = {'X-TBA-Auth-Key': apiKey}
YEAR = datetime.date.today().year
print(type(YEAR))

def apiCall(suffix: str) -> str:
    """Make an API call to Statbotics."""
    base = "https://api.statbotics.io/v1"
    url = base + suffix
    return requests.get(url, headers=headers).text

for i in argv:
    eloYears = []
    for j in range(2002, YEAR + 1): #this may break early in january, but it's fine
        eventName = str(j) + str(i)
        try:
            rawEvent = json.loads(apiCall("/event/" + eventName))
            if len(rawEvent) != 0:
                eloYears.append(rawEvent[0]["elo_mean"])
        except KeyError:
            continue
    print(i, "Average:", round(sum(eloYears)/len(eloYears), 2))
