#!/bin/bash
curl --silent "https://www.thebluealliance.com/event/$1" | grep -A1 team-name\" | grep href | grep -Eo "m\/[0-9]*" | sed "s/m\///" | tee /dev/tty | pbcopy

