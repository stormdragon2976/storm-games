#!/bin/bash

#If there is more than one command line arg something is wrong
if [ $# -gt 1 ] ; then
echo "usage:
$0 godname"
exit 1
fi

#set godName variable if it was passed from the command line
if [ $# -eq 1 ] ; then
godName="$1"
fi

#read from file if it exists, and name wasn't passed in on command line
if [ -f .godville-trackerrc -a $# -eq 0 ] ; then
source .godville-trackerrc
fi

#if name is not set in file, prompt for it here
if [ -z "$godName" ] ; then
read -p "Please enter the god's name? " godName
fi

godvilleInfo="$(curl -Ss "http://godvillegame.com/gods/api/${godName}.json")"
clear
#remove most of the json stuff
godvilleInfo="$(echo "$godvilleInfo" | sed -e 's/":"/ /g' -e 's/","/\n/g')"
godvilleInfo="$(echo "$godvilleInfo" | sed -e 's/":/ /g' -e 's/,"/\n/g')"
godvilleInfo="$(echo "$godvilleInfo" | sed -e 's/{"//g' -e 's/"}//g')"
echo "$godvilleInfo"
exit 0
