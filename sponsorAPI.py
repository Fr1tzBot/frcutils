from ast import arg
from sys import argv
import requests
import re
import json
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

argv = argv[1:]
headers = {'X-TBA-Auth-Key': apiKey}

def apiCall(suffix: str) -> str:
    base = "https://www.thebluealliance.com/api/v3/"
    url = base + suffix
    return requests.get(url, headers=headers).text

def getSponsors(team: str) -> dict:
    suffix = "team/frc" + team
    return json.loads(apiCall(suffix))["name"]

def multisplit(string: str, toSplit: list) -> list:
    for i in toSplit:
        string = string.replace(i, "\n")
    outList = string.split("\n")
    for i in range(len(outList)):
        outList[i] = outList[i].strip()
    return outList
    

def parseSponsors(sponsors: str) -> str:
    sponsors = sponsors.lower()
    schoolNameList = ["school", "preparatory", "academy"]
    for j in schoolNameList:
        if j in sponsors:
            andPosition = None
            for i in reversed(list(range(sponsors.index(j)))):
                if sponsors[i] == "&":
                    andPosition = i
                    break

            if andPosition is None:
                break

            for i in range(andPosition, len(sponsors)):
                if sponsors[i] == "&":
                    sponsors = list(sponsors)
                    sponsors[i] = "\n"
                    sponsors = "".join(sponsors)
        
        
    return multisplit(sponsors, ["/"])#[";", "&", "/"])

def csv(teamNumber: int, sponsors: list):
    return str(teamNumber) + "," + ",".join(sponsors)

for i in range(4847,8899):
    try:
        a = csv(i, parseSponsors(getSponsors(str(i))))
    except KeyError:
        continue
    if a == str(i) + ",team " + str(i):
        continue
    print(a)

#print(csv(argv[0], parseSponsors(getSponsors(str(argv[0])))))
# print(getSponsors(str(argv[0])))