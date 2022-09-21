#!/usr/bin/env python
from sys import argv
import os
import json
argv = argv[1:]
output = {}
for i in os.listdir("teams/"):
    with open("teams/" + i) as f:
        output[i] = f.read().split("\n")

print(json.dumps(output, indent=4))
