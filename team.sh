#!/bin/bash

TBA_LINK="https://www.thebluealliance.com/team/$1/"
TEAM_PAGE="$(curl --silent "$TBA_LINK")"

#grabSocial() {  }

printf "Team Name: "
echo "$TEAM_PAGE" | grep "<title>" | xargs | sed "s/<title>//" | sed "s/ - .*//" | tee /dev/tty | pbcopy
read

echo "Rookie Year:"
echo "$TEAM_PAGE" | grep "rookie" | grep -Eo "Rookie Year: [0-9]{4}" | sed s"/Rookie Year: //" | tee /dev/tty | pbcopy
read

echo "TBA link:"
echo "$TBA_LINK" | tee /dev/tty | pbcopy
read

printf "Team Website: "
echo "$TEAM_PAGE" | grep "team-website" | grep -o ">http.*<\/a" | sed "s/>//" | sed "s/<\/a//" | tee /dev/tty | pbcopy
read

printf "Team Youtube: "
echo "$TEAM_PAGE" | grep "youtube-channel" | grep -o "http.*\" c" | sed "s/\" c//" | tee /dev/tty | pbcopy
read

printf "Team Twitter: "
echo "$TEAM_PAGE" | grep "twitter-profile" | grep -o "http.*\" c" | sed "s/\" c//" | tee /dev/tty | pbcopy
read

printf "Team Facebook: "
echo "$TEAM_PAGE" | grep "facebook-profile" | grep -o "http.*\" c" | sed "s/\" c//" | tee /dev/tty | pbcopy
read

printf "Team Insta: "
echo "$TEAM_PAGE" | grep "instagram-profile" | grep -o "http.*\" c" | sed "s/\" c//" | tee /dev/tty | pbcopy
read

printf "Team Github: "
echo "$TEAM_PAGE" | grep "github-profile" | grep -o "http.*\" c" | sed "s/\" c//" | tee /dev/tty | pbcopy

printf "\n"

