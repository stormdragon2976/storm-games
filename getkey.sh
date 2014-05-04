#!/bin/bash

# Reset terminal to current state when we exit.
trap "stty $(stty -g)" EXIT

# Disable echo and special characters, set input timeout to 0.2 seconds.
stty -echo -icanon time 2 || exit $?

# String containing all keypresses.
KEYS=""

# Set field separator to BELL (should not occur in keypresses)
IFS=$'\a'

# Input loop.
while [ 1 ]; do

    # Read more input from keyboard when necessary.
    while read -t 0 ; do
        read -s -r -d "" -N 1 -t 0.2 CHAR && KEYS="$KEYS$CHAR" || break
    done
    # If no keys to process, wait 0.05 seconds and retry.
    if [ -z "$KEYS" ]; then
        sleep 0.02
        continue
    fi

    # Check the first (next) keypress in the buffer.
    case "$KEYS" in
      $'\x1B\x5B\x41'*) # Up arrow
        KEYS="${KEYS##???}"
        KEY="Arrow_U"
        ;;
      $'\x1B\x5B\x42'*) # Down Arrow
        KEYS="${KEYS##???}"
        KEY="Arrow_D"
        ;;
      $'\x1B\x5B\x44'*) # Left Arrow
        KEYS="${KEYS##???}"
        KEY="Arrow_L"
        ;;
      $'\x1B\x5B\x43'*) # Right Arrow
        KEYS="${KEYS##???}"
        KEY="Arrow_R"
        ;;
      $'\x1B\x4F\x48'*) # Home
        KEYS="${KEYS##???}"
        KEY="Home"
        ;;
      $'\x1B\x5B\x31\x7E'*) # Home (Numpad)
        KEYS="${KEYS##????}"
        KEY="Home"
        ;;
      $'\x1B\x4F\x46'*) # End
        KEYS="${KEYS##???}"
        KEY="End"
        ;;
      $'\x1B\x5B\x34\x7E'*) # End (Numpad)
        KEYS="${KEYS##????}"
        KEY="End"
        ;;
      $'\x1B\x5B\x45'*) # 5 (Numpad)
        KEYS="${KEYS#???}"
        KEY="Numpad_5"
        ;;
      $'\x1B\x5B\x35\x7e'*) # PageUp
        KEYS="${KEYS##????}"
        KEY="Page_U"
        ;;
      $'\x1B\x5B\x36\x7e'*) # PageDown
        KEYS="${KEYS##????}"
        KEY="Page_D"
        ;;
      $'\x1B\x5B\x32\x7e'*) # Insert
        KEYS="${KEYS##????}"
        KEY="Insert"
        ;;
      $'\x1B\x5B\x33\x7e'*) # Delete
        KEYS="${KEYS##????}"
        KEY="Delete"
        ;;
      $'\n'*|$'\r'*) # Enter/Return
        KEYS="${KEYS##?}"
        KEY="Enter"
        ;;
      $'\t'*) # Tab
        KEYS="${KEYS##?}"
        KEY="Tab"
        ;;
      $'\x1B') # Esc (without anything following!)
        KEYS="${KEYS##?}"
        exit 0
        ;;
      $'\x1B'*) # Unknown escape sequences
        echo -n "Unknown escape sequence (${#KEYS} chars): \$'"
        echo -n "$KEYS" | od --width=256 -t x1 | sed -e '2,99 d; s|^[0-9A-Fa-f]* ||; s| |\\x|g; s|$|'"'|"
        KEYS=""
        ;;
      [$'\x01'-$'\x1F'$'\x7F']*) # Consume control characters
        KEYS="${KEYS##?}"
        ;;
      *) # Printable characters.
        KEY="${KEYS:0:1}"
        KEYS="${KEYS#?}"
        ;;
    esac
echo "$KEY"
done
