#!/bin/bash

TBA_LINK="https://www.thebluealliance.com/team/$1/"
TEAM_PAGE="$(curl --silent "$TBA_LINK")"


echo "$TEAM_PAGE" | grep "<title>" | xargs | sed "s/<title>//" | sed "s/ - .*//"

