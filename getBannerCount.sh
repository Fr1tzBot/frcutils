#!/bin/bash

getTeam() { curl --silent "https://www.thebluealliance.com/team/$1/history" | grep -c "<div class=\"banner\">"; }
echo "$1 $(getTeam $1)"

