#!/usr/bin/env bash

# mapfile -t ARR <sample.txt
mapfile -t ARR <input.txt
INDEX=-1
INCREASED=0

for LINE in "${ARR[@]}"; do
  PREVIOUS="${ARR["$INDEX"]}"
  echo "Previous: $PREVIOUS"
  echo "Current: $LINE"
  if [ $LINE -gt $PREVIOUS ]; then
    echo "Increased"
    INCREASED="$(($INCREASED + 1))"
  else
    echo "Decreased"
  fi
  INDEX="$(($INDEX + 1))"
done

echo "Increased $INCREASED times."
