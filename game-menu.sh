#!/bin/bash

export DIALOGOPTS='--no-lines --visit-items'
cols=$(tput cols)
lines=$(tput lines)
path="$(realpath "$0")"
path="${path%/*}"
declare -A gameList
for i in $path/*/ ; do
i="${i::-1}"
gameList[${i##*/}]="${i}"
done
gameList[exit]="Exit"
while : ; do
game="$(dialog --backtitle "Storm Games" \
--menu "Select A Game" $((lines - 5)) $cols $((lines / 2)) $(
for i in ${!gameList[@]} ; do
echo "$i"
echo '|'
done) --stdout)"
if [[ "$game" != "exit" && -n "$game" ]]; then
cd "${gameList[$game]}"
./$game""
echo
read -n1 -p "Press any key to continue" continue
else
break
fi
done
exit 0
