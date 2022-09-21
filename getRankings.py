import requests
import json
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

def apiCall(suffix: str) -> str:
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    return requests.get(base + suffix, headers=headers).text

for i in json.loads(apiCall("/event/2022mikk3/rankings"))["rankings"]:
    print(i["team_key"][3:] + "," + str(i["rank"]))